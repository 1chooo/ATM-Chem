from Load import Tool

data_path = r"/Users/linchunho/Developer/ATM-Chem/src/data/monthly_mean/"
type = "co2"
skip_rows = 53
data_type = ["year", "month", "date", "avg", "de-s", "day", "std", "unc"]

data = Tool.loadData(data_path, type, skip_rows, data_type)

print(data)