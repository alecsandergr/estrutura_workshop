import os
import glob

import pandas as pd

from typing import List

"""
Função para ler os arquivos de uma pasta 
data/input e retorn uma lista de dataframes

args: input_path (str): caminho da pasta com os arquivos

return: lista de dataframes
"""

def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(input_path, '*.xlsx'))

    data_frame_list = [pd.read_excel(file) for file in all_files]

    return data_frame_list

if __name__ == '__main__':
    data_frame_list = extract_from_excel(input_path)
    print(data_frame_list)