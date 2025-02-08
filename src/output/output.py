import os
import pandas as pd

from src.downloader.interfaces.downloader_interface import IDownloadStrategy
from src.output.interfaces.output_interface import IOutputStrategy

class Output(IOutputStrategy):
    def __init__(self, output_file):
        self.output_file = output_file
    
    def save_to_csv(self, data):
        if data:
            df = pd.concat(data)
            if os.path.exists(self.output_file):
                df.to_csv(self.output_file, mode='a', header=False, index=False)
            else:
                df.to_csv(self.output_file, index=False)
            print(f"Data saved to {self.output_file}")
        else:
            print("No data to save")
        
        

        
