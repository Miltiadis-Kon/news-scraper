from abc import ABC, abstractmethod

class IOutputStrategy(ABC):
    
    @abstractmethod
    def save_to_csv(self, data, file_path):
        """ Save the data to a CSV file. """
        pass