import pandas as pd
from pathlib import Path

# ----------------------------
# File Paths
# ----------------------------
RAW_FILE = "../data/raw/2019-Nov.csv"
OUTPUT_FILE = "../data/processed/cleaned_data.csv"

# Create processed folder if it doesn't exist
Path("../data/processed").mkdir(parents=True, exist_ok=True)

CHUNK_SIZE = 100000

print("=" * 60)
print("Starting Data Cleaning...")
print("=" * 60)

total_rows = 0
total_cleaned = 0
first_chunk = True

for chunk in pd.read_csv(RAW_FILE, chunksize=CHUNK_SIZE):

    # Convert event_time to datetime
    chunk["event_time"] = pd.to_datetime(chunk["event_time"])

    # Fill missing values
    chunk["brand"] = chunk["brand"].fillna("Unknown")
    chunk["category_code"] = chunk["category_code"].fillna("Unknown")

    # Remove duplicates
    chunk = chunk.drop_duplicates()

    # Save cleaned chunk
    chunk.to_csv(
        OUTPUT_FILE,
        mode="w" if first_chunk else "a",
        header=first_chunk,
        index=False
    )

    total_rows += CHUNK_SIZE
    total_cleaned += len(chunk)

    print(f"Processed approximately {total_rows:,} rows...")

    first_chunk = False

print("\nCleaning Completed Successfully!")
print(f"Total Cleaned Rows: {total_cleaned:,}")
print(f"Saved to: {OUTPUT_FILE}")