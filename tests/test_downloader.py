import os
import pytest
from datetime import datetime
from src.downloader.downloader import Downloader

@pytest.fixture
def downloader():
    return Downloader()

def test_download_success(downloader, mocker):
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.status_code = 200
    mock_response.return_value.content = b'Test content'

    file_path = downloader.download('01', '01', '2023')
    assert os.path.exists(file_path)
    assert file_path.endswith('20230101_data.xls')

    with open(file_path, 'rb') as file:
        content = file.read()
        assert content == b'Test content'

    os.remove(file_path)

def test_download_failure(downloader, mocker):
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.status_code = 404

    with pytest.raises(Exception) as excinfo:
        downloader.download('01', '01', '2023')
    assert "Failed to download file" in str(excinfo.value)

#TODO: Fix this test
def test_download_files(downloader, mocker):
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.status_code = 200
    mock_response.return_value.content = b'Test content'

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 2, 3)
    downloader.download_files(start_date, end_date)

    for day in range(1, 4):
        file_path = os.path.join(downloader.download_dir, f"202301{day:02d}_data.xls")
        assert os.path.exists(file_path)
        os.remove(file_path)