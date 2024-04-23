import pandas as pd

df = pd.read_excel("data.xlsx")


for i, row in df.iterrows():
    print(f" {row.iloc[0]} {row.iloc[1]}")
