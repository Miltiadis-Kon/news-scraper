# data-processor/data-processor/README.md

# Data Processor Project

This project is designed to download daily realized data regarding the Greek Power Network system, process the data, and output it in a structured CSV format.

## Project Structure

```
data-processor
├── src
│   ├── __init__.py
│   ├── downloader
│   │   ├── __init__.py
│   │   ├── interfaces
│   │   │   ├── __init__.py
│   │   │   └── downloader_interface.py
│   │   └── downloader.py
│   ├── processor
│   │   ├── __init__.py
│   │   ├── interfaces
│   │   │   ├── __init__.py
│   │   │   └── processor_interface.py
│   │   └── processor.py
│   ├── output
│   │   ├── __init__.py
│   │   ├── interfaces
│   │   │   ├── __init__.py
│   │   │   └── output_interface.py
│   │   └── output.py
│   └── config.py
├── data
│   ├── input
│   └── output
├── tests
│   └── __init__.py
├── requirements.txt
└── README.md
```

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/greek-power-network-data-processor.git
    cd greek-power-network-data-processor
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the main script**:
    ```sh
    python main.py
    ```

    This will download the data from the specified date range (2023-01-01 to 2023-10-31), process it, and save the output to a CSV file in the [output](http://_vscodecontentref_/20) directory.

## Configuration

The configuration settings are located in the [config.py](http://_vscodecontentref_/21) file. You can modify the following settings:

- [START_DATE](http://_vscodecontentref_/22): The start date for downloading data (format: "YYYY-MM-DD").
- [END_DATE](http://_vscodecontentref_/23): The end date for downloading data (format: "YYYY-MM-DD").
- [BASE_URL](http://_vscodecontentref_/24): The base URL for downloading Excel files.
- [INPUT_DIR](http://_vscodecontentref_/25): The directory for storing downloaded files.
- [OUTPUT_DIR](http://_vscodecontentref_/26): The directory for storing the output CSV file.

## Project Components

### Downloader

The [Downloader](http://_vscodecontentref_/27) class is responsible for downloading the Excel files from the specified URLs based on the date range. It uses the [requests](http://_vscodecontentref_/28) library to fetch the files and saves them to the [input](http://_vscodecontentref_/29) directory.

### Processor

The [Processor](http://_vscodecontentref_/30) class reads the downloaded Excel files, extracts the relevant data (hourly NET LOAD), and returns it as a DataFrame. It also deletes the processed files after extraction.

### Output

The [Output](http://_vscodecontentref_/31) class saves the processed data into a final CSV file with the headers: Date, Hour, Net Load.

### Tests

The [tests](http://_vscodecontentref_/32) directory contains test cases for the [Downloader](http://_vscodecontentref_/33) class. You can run the tests using [pytest](http://_vscodecontentref_/34):

```sh
pytest tests/test_downloader.py -v
```
## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


