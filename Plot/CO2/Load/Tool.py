import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob
from PIL import Image


class Tool :

    def loadData(data_path, type, skip_rows, data_type) :

        os.chdir(data_path)
        for file in os.listdir() :
            if file.startswith(f"{type}") :
                file_path = f"{data_path}/{file}"
                data = pd.read_csv(file_path, skiprows=skip_rows, sep="\s+")
                data = data.replace(-0.99, 0)
                data = data.replace(-9.99, 0)
                data = data.replace(-1   , 0)
                data.columns = data_type

        return data