import os
import pandas as pd

from src.config import SEPERATOR
from src.output.interfaces.output_interface import IOutputStrategy

class Output(IOutputStrategy):
    def __init__(self, output_file):
        self.output_file = output_file
    
    def save_to_csv(self, data): 
        if data:
            df = pd.concat(data) # Concatenate the list of dataframes
            df = df[['Date', 'Hour', 'Net Load']] # Ensure the DataFrame has the correct columns
            if os.path.exists(self.output_file):
                df.to_csv(self.output_file, mode='a', header=False, index=False,sep=SEPERATOR) # Append the data to the existing file
            else:
                df.to_csv(self.output_file, index=False,sep=SEPERATOR) # Save the data to a new file
        else:
            print("No data to save")