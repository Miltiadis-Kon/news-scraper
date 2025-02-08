# Data Processor Project

This project is designed to download daily realized data regarding the Greek Power Network system, process the data, and output it in a structured CSV format.

## Results
Below is a snapshot of the first and last rows when the.csv file is imported to excel.
[Figure](images\first_rows.png)
[Figure2](images\last_rows.png)

Output file can be found [here](https://github.com/Miltiadis-Kon/news-scraper/tree/main/data/output)
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
    git clone https://github.com/Miltiadis-Kon/news-scraper.git
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

    This will download the data from the specified date range (2023-01-01 to 2023-10-31), process it, and save the output to a CSV file in the [output](https://github.com/Miltiadis-Kon/news-scraper/tree/main/data/output) directory.

## Configuration

The configuration settings are located in the [config.py](https://github.com/Miltiadis-Kon/news-scraper/blob/main/src/config.py) file. You can modify the following settings:

- [START_DATE](https://github.com/Miltiadis-Kon/news-scraper/blob/main/src/config.py#L4): The start date for downloading data (format: "YYYY-MM-DD").
- [END_DATE](https://github.com/Miltiadis-Kon/news-scraper/blob/main/src/config.py#L5): The end date for downloading data (format: "YYYY-MM-DD").
- [BASE_URL](https://github.com/Miltiadis-Kon/news-scraper/blob/main/src/config.py#L8): The base URL for downloading Excel files.

## Project Components

### Downloader

The [Downloader](https://github.com/Miltiadis-Kon/news-scraper/blob/main/src/downloader/downloader.py) class is responsible for downloading the Excel files from the specified URLs based on the date range. It uses the [requests](https://github.com/psf/requests) library to fetch the files and saves them to the [input](https://github.com/Miltiadis-Kon/news-scraper/tree/main/data/input) directory.

### Processor

The [Processor](https://github.com/Miltiadis-Kon/news-scraper/blob/main/src/processor/processor.py) class reads the downloaded Excel files, extracts the relevant data (hourly NET LOAD), and returns it as a DataFrame. It also deletes the processed files after extraction.

### Output

The [Output](https://github.com/Miltiadis-Kon/news-scraper/blob/main/src/output/output.py) class saves the processed data into a final CSV file with the headers: Date, Hour, Net Load.

### Tests

The [tests](https://github.com/Miltiadis-Kon/news-scraper/tree/main/tests) directory contains test cases for the [Downloader](https://github.com/Miltiadis-Kon/news-scraper/blob/main/src/downloader/downloader.py) class. You can run the tests using [pytest](https://github.com/pytest-dev/pytest):

```sh
pytest tests/test_downloader.py -v
```
## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


