import requests
import os
from src.config import BASE_URL
from datetime import timedelta
from tqdm import tqdm

from src.downloader.interfaces.downloader_interface import IDownloadStrategy
from src.output.interfaces.output_interface import IOutputStrategy
from src.processor.interfaces.processor_interface import IProcessorStrategy

class Downloader(IDownloadStrategy):
    def __init__(self, processing_strategy: IProcessorStrategy = None, output_strategy: IOutputStrategy = None):
        self.base_url = BASE_URL
        self.download_dir = os.path.join(os.path.dirname(__file__), '../../data/input')
        self.processing_strategy = processing_strategy  # Initialize the processing strategy
        self.output_strategy = output_strategy  # Initialize the output strategy

        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

    def download(self, month, day, year):
        url = self.base_url.format(month=month.zfill(2), day=day.zfill(2), year=year)  # Format the URL with the current date
        response = requests.get(url)

        if response.status_code == 200:
            file_path = os.path.join(self.download_dir, f"{year}{month}{day}_data.xls")  # Save the file with the current date
            with open(file_path, 'wb') as file:
                file.write(response.content)  # Write the content of the response to the file
            return file_path
        else:
            raise Exception(f"Failed to download file from {url}. Status code: {response.status_code}")

    def download_files(self, start_date, end_date):
        output_data = []
        current_date = start_date
        total_days = (end_date - start_date).days + 1  # Calculate total number of days

        with tqdm(total=total_days, desc="Downloading files", unit="file") as pbar:
            while current_date <= end_date:
                month = current_date.strftime("%m")
                day = current_date.strftime("%d")
                year = current_date.strftime("%Y")
                try:
                    file_path = self.download(month, day, year)  # Download the file
                    if self.processing_strategy:
                        result_df = self.processing_strategy.process_csv(file_path)  # Process the downloaded file
                        if result_df is not None:
                            self.output_strategy.save_to_csv([result_df])  # Save the processed data to a CSV file
                        else:
                            print(f"Skipping {current_date.date()}")
                except Exception as e:
                    print(e)
                current_date += timedelta(days=1)  # Move to the next day
                pbar.update(1)  # Update the progress bar
        return output_data