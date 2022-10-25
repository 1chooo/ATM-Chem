from Load import Tool

data_path = r"/Users/linchunho/Developer/ATM-Chem/src/data/monthly_mean/"
imgs_path = r"/Users/linchunho/Developer/ATM-Chem/src/imgs/CO2/"
type = "co2"
skip_rows = 53
data_type = ["year", "month", "date", "avg", "de-s", "day", "std", "unc"]

data = Tool.load_data(data_path, type, skip_rows, data_type)

water_mark = Tool.add_water_mark(imgs_path)

print(data)