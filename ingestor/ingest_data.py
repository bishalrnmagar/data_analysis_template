from abc import ABC, abstractmethod

import pandas as pd

# Abstract class for data ingestion
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, path: str) -> pd.DataFrame:
        """ Abstract method to ingest data from given file """
        pass

# Concrete class for Zipped file
class CsvDataIngestor(DataIngestor):
    def ingest(self, path: str) -> pd.DataFrame:
        """ Extract content from .csv file and return as pandas dataframe """
        pass

# Implement a factory to create data ingestor
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(self, file_ext: str):
        """ Return appropriate data ingestor based on file extension """
        if file_ext == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError("No ingestion available for file extension : {file_ext}")

if __name__ == "__main__":
    pass