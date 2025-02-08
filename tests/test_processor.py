import pytest
import os
import pandas as pd
from src.processor.processor import Processor

@pytest.fixture
def processor():
    return Processor()

def test_process_csv(processor, tmpdir):
    # Create a sample Excel file
    file_path = os.path.join(tmpdir, "20230101_data.xls")
    df = pd.DataFrame({
        'Unnamed: 0': ['NET LOAD'],
        'Unnamed: 1': [4902],
        'Unnamed: 2': [4429],
        'Unnamed: 3': [4267],
        'Unnamed: 4': [4129],
        'Unnamed: 5': [4176],
        'Unnamed: 6': [4367],
        'Unnamed: 7': [4915],
        'Unnamed: 8': [5847],
        'Unnamed: 9': [5804],
        'Unnamed: 10': [5039],
        'Unnamed: 11': [4447],
        'Unnamed: 12': [4049],
        'Unnamed: 13': [3716],
        'Unnamed: 14': [3635],
        'Unnamed: 15': [3599],
        'Unnamed: 16': [4255],
        'Unnamed: 17': [5210],
        'Unnamed: 18': [6330],
        'Unnamed: 19': [7147],
        'Unnamed: 20': [7390],
        'Unnamed: 21': [7320],
        'Unnamed: 22': [6872],
        'Unnamed: 23': [6310],
        'Unnamed: 24': [5753]
    })
    df.to_excel(file_path, index=False)

    result_df = processor.process_csv(file_path)
    assert result_df is not None
    assert len(result_df) == 24
    assert result_df.iloc[0]['Net Load'] == 4902.0

def test_process_csv_missing_net_load(processor, tmpdir):
    # Create a sample Excel file without NET LOAD
    file_path = os.path.join(tmpdir, "20230101_data.xls")
    df = pd.DataFrame({
        'Unnamed: 0': ['OTHER LOAD'],
        'Unnamed: 1': [4902]
    })
    df.to_excel(file_path, index=False)

    result_df = processor.process_csv(file_path)
    assert result_df is None