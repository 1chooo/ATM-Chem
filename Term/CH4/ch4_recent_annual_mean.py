import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

data_path = r"/Users/linchunho/Developer/ATM-Chem/src/data/monthly_mean/"
os.chdir(data_path)

for file in os.listdir() :
    if file.startswith(f"ch4") :
    # if file.endswith(f"mlo.txt") : 
        file_path = f"{data_path}/{file}"
        data = pd.read_csv(file_path, skiprows=478, sep="\s+")
        data = data.replace(-0.99, 0)
        data = data.replace(-9.99, 0)
        data = data.replace(-1   , 0)
        data.columns = ["year", "month", "date", "avg", "avg_unc", "trends", "unc"]

        print(data)