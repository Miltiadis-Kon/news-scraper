import pytest
import os
import sys
import tempfile
from src.downloader.downloader import Downloader


# Add the project root directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

@pytest.fixture
def temp_download_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def downloader(temp_download_dir):
    downloader = Downloader()
    downloader.download_dir = temp_download_dir
    return downloader

def test_download_success(downloader):
    # Assuming the URL is valid and the file exists for the test
    month = "01"
    day = "01"
    year = "2023"
    file_path = downloader.download(month, day, year)
    assert os.path.exists(file_path)
    assert file_path.endswith("_data.xls")

def test_download_failure(downloader):
    month = "99"  # Invalid month
    day = "01"
    year = "2023"
    with pytest.raises(Exception):
        downloader.download(month, day, year)

def test_download_files(downloader):
    from datetime import datetime, timedelta

    start_date = datetime(2023, 1, 1)
    end_date = start_date + timedelta(days=2)  # Download for 3 days
    downloader.download_files(start_date, end_date)

    # Check if files were downloaded
    for i in range(3):
        date = start_date + timedelta(days=i)
        month = date.strftime("%m")
        day = date.strftime("%d")
        year = date.strftime("%Y")
        file_path = os.path.join(downloader.download_dir, f"{year}{month}{day}_data.xls")
        assert os.path.exists(file_path)