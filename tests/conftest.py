import pytest
import os
import sys
import tempfile

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.downloader.downloader import Downloader
from src.processor.processor import Processor
from src.output.output import Output

@pytest.fixture
def temp_download_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def downloader(temp_download_dir):
    downloader = Downloader()
    downloader.download_dir = temp_download_dir
    return downloader

@pytest.fixture
def processor():
    return Processor()

@pytest.fixture
def output(tmpdir):
    output_file = os.path.join(tmpdir, "net_load_data.csv")
    return Output(output_file=output_file)