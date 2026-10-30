import pandas as pd

# Read only first 5 rows (don't load the whole file)
file_path = "../data/raw/2019-Nov.csv"

df = pd.read_csv(file_path, nrows=5)

print("=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)
print(df)

print("\n")

print("=" * 60)
print("COLUMN NAMES")
print("=" * 60)
print(df.columns.tolist())