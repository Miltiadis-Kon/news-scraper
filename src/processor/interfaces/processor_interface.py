from abc import ABC, abstractmethod

class IProcessorStrategy(ABC):
    
    @abstractmethod
    def process_csv(self, file_path: str) -> list:
        """Process the CSV file and return the extracted data."""
        pass
    
    
    @abstractmethod
    def clean_up(self, file_path: str) -> None:
        """Delete the specified file after processing."""
        pass