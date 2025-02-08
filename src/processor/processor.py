import pandas as pd
import os
from datetime import datetime
from src.processor.interfaces.processor_interface import IProcessorStrategy

class Processor(IProcessorStrategy):
    def process_csv(self, file_path):
        try:
            sheet_name = 'System_Production'
            # Read the XLS file
            df = pd.read_excel(file_path,sheet_name=sheet_name)
            
            # Extract date from filename (20230201 -> 2023-02-01)
            file_date = os.path.basename(file_path).split('_')[0]
            date = datetime.strptime(file_date, '%Y%m%d').strftime('%Y-%m-%d')  
            
            # Find the row containing "NET LOAD str"
            net_load_row = df[df.iloc[:, 1] == 'NET LOAD']
                        
            if net_load_row.empty:
                raise ValueError("NET LOAD row not found in the file")
            
            # Extract the 24 hourly values (columns 1-24)
            hourly_values = net_load_row.iloc[0, 2:26].values
            
            # Create a new DataFrame with the required format
            processed_data = []
            for hour, value in enumerate(hourly_values, start=1):
                processed_data.append({
                    'Date': date,
                    'Hour': hour,
                    'Net Load': float(value)
                })
            
            result_df = pd.DataFrame(processed_data)
            self.clean_up(file_path)
            return result_df
            
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")
            return None
    
    def clean_up(self, file_path):
        import os
        os.remove(file_path)