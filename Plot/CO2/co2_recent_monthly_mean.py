import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

data_path = r"/Users/linchunho/Developer/ATM-Chem/src/data/monthly_mean/"
os.chdir(data_path)

for file in os.listdir() :
    if file.endswith(f"mlo.txt") :
        file_path = f"{data_path}/{file}"
        data = pd.read_csv(file_path, skiprows=771, sep="\s+")
        data = data.replace(-0.99, 0)
        data = data.replace(-9.99, 0)
        data = data.replace(-1   , 0)
        data.columns = ["year", "month", "date", "avg", "de-s", "day", "std", "unc"]

        print(data)

plt.figure(figsize=(20, 15))
plt.plot(data["date"], data["de-s"], "k-o")
plt.plot(data["date"], data["avg"], "r-o")

plt.xlabel("Year", fontsize=16)
plt.ylabel("CO2 mole fraction (ppm)", fontsize=16)
plt.title("Recently monthly Mean CO2 at Mauna Loa Observatory", fontsize=20)

plt.grid()
plt.savefig("../../imgs/CO2/co2_recent_monthly_mean.jpg", dpi=300)
plt.show()