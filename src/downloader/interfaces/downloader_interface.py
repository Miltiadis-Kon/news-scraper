from abc import ABC, abstractmethod

class IDownloadStrategy(ABC):
    @abstractmethod
    def download(self, url: str, local_filename: str) -> None:
        """ Retrieve data from a URL and save it to a local file. """
        pass
    
    @abstractmethod
    def download_files(self, urls: list) -> None:
        """ Iterate over a list of URLs and download each one. """
        pass