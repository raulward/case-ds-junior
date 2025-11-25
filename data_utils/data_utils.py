import pandas as pd
import numpy as np


class DataUtils:
    """
    Lidar com alguns problemas frequentes relacionados aos dados

    """

    def __init__(self):
        pass

    def read_data(file: str, sep: str = ';', base_path: str = '../data') -> pd.DataFrame:
            """
            Essa função tem a finalidade de realizar a leitura dos arquivos passados via parâmetro
            """
            final_path = base_path + file
            df = pd.read_csv(final_path, sep=sep)
            return df
