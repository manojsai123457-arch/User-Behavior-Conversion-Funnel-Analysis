import pandas as pd
import random

INPUT_FILE = "../data/raw/2019-Nov.csv"
OUTPUT_FILE = "../data/processed/analysis_data.csv"

CHUNK_SIZE = 100000
TARGET_ROWS = 500000

print("=" * 60)
print("Creating Analysis Dataset...")
print("=" * 60)

sample_chunks = []
rows_collected = 0

for chunk in pd.read_csv(INPUT_FILE, chunksize=CHUNK_SIZE):

    # ---------------- Cleaning ----------------
    chunk["event_time"] = pd.to_datetime(chunk["event_time"])
    chunk["brand"] = chunk["brand"].fillna("Unknown")
    chunk["category_code"] = chunk["category_code"].fillna("Unknown")
    chunk = chunk.drop_duplicates()

    # Sample only 7.5% of each chunk
    sample_size = int(len(chunk) * 0.075)

    sampled = chunk.sample(n=sample_size, random_state=42)

    sample_chunks.append(sampled)

    rows_collected += len(sampled)

    print(f"Collected {rows_collected:,} rows")

    if rows_collected >= TARGET_ROWS:
        break

analysis_df = pd.concat(sample_chunks, ignore_index=True)

# Keep exactly 500,000 rows
analysis_df = analysis_df.sample(n=TARGET_ROWS, random_state=42)

analysis_df.to_csv(OUTPUT_FILE, index=False)

print("\n========================================")
print("Analysis Dataset Created Successfully!")
print("Shape:", analysis_df.shape)
print("Saved:", OUTPUT_FILE)