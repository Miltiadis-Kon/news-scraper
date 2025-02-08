import requests
import os
from src.config import BASE_URL
import calendar

from src.downloader.interfaces.downloader_interface import IDownloadStrategy
from src.output.interfaces.output_interface import IOutputStrategy
from src.processor.interfaces.processor_interface import IProcessorStrategy

class Downloader(IDownloadStrategy):
    def __init__(self, processing_strategy: IProcessorStrategy = None,output_strategy: IOutputStrategy = None ):
        self.base_url = BASE_URL
        self.download_dir = os.path.join(os.path.dirname(__file__), '../../data/input')
        self.processing_strategy = processing_strategy
        self.output_strategy = output_strategy
        
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
  
    def download(self, month, day, year):
        url = self.base_url.format(month=month.zfill(2), day=day.zfill(2), year=year)
        response = requests.get(url)

        if response.status_code == 200:
            file_path = os.path.join(self.download_dir, f"{year}{month}{day}_data.xls")
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return file_path
        else:
            raise Exception(f"Failed to download file from {url}. Status code: {response.status_code}")

    def download_files(self, start_date, end_date):
        output_data = []
        current_date = start_date
        _,days_in_month = calendar.monthrange(current_date.year, current_date.month)
        while current_date <= end_date:
            month = current_date.strftime("%m")
            day = current_date.strftime("%d")
            year = current_date.strftime("%Y")
            try:
                file_path= self.download(month, day, year)
                print(f"Sucesfully downloaded data for {current_date.date()}!")
                if self.processing_strategy:
                    result_df = self.processing_strategy.process_csv(file_path)
                    if result_df is not None:
                        self.output_strategy.save_to_csv([result_df])
                    else:
                        print(f"Skipping {current_date.date()}")
                        
            except Exception as e:
                print(e)
            current_date = current_date.replace(day=current_date.day + 1) if current_date.day < days_in_month else current_date.replace(month=current_date.month + 1, day=1)
        return output_data
    
