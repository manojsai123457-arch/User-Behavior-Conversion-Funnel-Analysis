import pandas as pd

file_path = "../data/raw/2019-Nov.csv"

print("Reading sample...")

df = pd.read_csv(file_path, nrows=1000)

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nUnique Event Types:")
print(df["event_type"].unique())

print("\nMemory Usage:")
print(df.memory_usage(deep=True))