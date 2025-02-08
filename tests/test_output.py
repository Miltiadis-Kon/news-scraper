import pytest
import os
import pandas as pd
from src.output.output import Output

@pytest.fixture
def output(tmpdir):
    output_file = os.path.join(tmpdir, "net_load_data.csv")
    return Output(output_file=output_file)

def test_save_to_csv(output):
    data = pd.DataFrame({
        'Date': ['2023-01-01'] * 24,
        'Hour': list(range(1, 25)),
        'Net Load': [4902, 4429, 4267, 4129, 4176, 4367, 4915, 5847, 5804, 5039, 4447, 4049, 3716, 3635, 3599, 4255, 5210, 6330, 7147, 7390, 7320, 6872, 6310, 5753]
    })

    output.save_to_csv([data])
    assert os.path.exists(output.output_file)

    saved_data = pd.read_csv(output.output_file)
    assert len(saved_data) == 24
    assert saved_data.iloc[0]['Net Load'] == 4902.0

def test_save_to_csv_append(output):
    data1 = pd.DataFrame({
        'Date': ['2023-01-01'] * 24,
        'Hour': list(range(1, 25)),
        'Net Load': [4902, 4429, 4267, 4129, 4176, 4367, 4915, 5847, 5804, 5039, 4447, 4049, 3716, 3635, 3599, 4255, 5210, 6330, 7147, 7390, 7320, 6872, 6310, 5753]
    })

    data2 = pd.DataFrame({
        'Date': ['2023-01-02'] * 24,
        'Hour': list(range(1, 25)),
        'Net Load': [4902, 4429, 4267, 4129, 4176, 4367, 4915, 5847, 5804, 5039, 4447, 4049, 3716, 3635, 3599, 4255, 5210, 6330, 7147, 7390, 7320, 6872, 6310, 5753]
    })

    output.save_to_csv([data1])
    output.save_to_csv([data2])
    assert os.path.exists(output.output_file)

    saved_data = pd.read_csv(output.output_file)
    assert len(saved_data) == 48
    assert saved_data.iloc[0]['Net Load'] == 4902.0
    assert saved_data.iloc[24]['Net Load'] == 4902.0