from datetime import datetime
from src.downloader.downloader import Downloader
from src.processor.processor import Processor
from src.output.output import Output
import os
from src.config import START_DATE, END_DATE

def main():
    try:
        # Initialize the processor
        processor = Processor()
        
        output = Output(output_file=os.path.join(os.path.dirname(__file__), f"data/output/net_load{datetime.now().strftime('_%Y_%m_%d_%H%M')}.csv"))

        # Initialize the downloader with the processor as the processing strategy
        downloader = Downloader(processing_strategy=processor, output_strategy=output)
        
        # Define date range
        start_date = datetime.strptime(START_DATE, "%Y-%m-%d")
        end_date = datetime.strptime(END_DATE, "%Y-%m-%d")

        print(f"Downloading data from {start_date.date()} to {end_date.date()}")
        
        downloader.download_files(start_date, end_date)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        

if __name__ == "__main__":
    main()