import pandas as pd
import numpy as np
import os

class CSVDataVisualizer:
    '''
    Description
    '''

    def __init__(self, file_path: str) -> None:
        # check file path exist
        if not isinstance(file_path, str):
            raise ValueError('Input file_path should be string.')

        if not os.path.exists(file_path):
            raise ValueError('Input path not exists')
        

        self.raw_data: pd.DataFrame = pd.read_csv(file_path)
        pass

    def clean_data(self):
        pass

    def preview_data(self):
        return self.raw_data.head()
    
    def plot_data_correlation(self) -> np.ndarray:
        pass

    
    
    '''
    plot data head, a subset of data, how many Nan: check whether need to drop / check whether need to scaler
    '''