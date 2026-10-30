import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -------------------------
# Paths
# -------------------------
DATA_FILE = "../data/processed/analysis_data.csv"
IMAGES_DIR = Path("../images")
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------
# Load data
# -------------------------
print("=" * 60)
print("Loading data...")
print("=" * 60)

df = pd.read_csv(DATA_FILE)

print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())
print("\nEvent types:\n", df["event_type"].value_counts())

# -------------------------
# Basic cleaning for analysis
# -------------------------
df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")
df["date"] = df["event_time"].dt.date

df["brand"] = df["brand"].fillna("Unknown")
df["category_code"] = df["category_code"].fillna("Unknown")

# -------------------------
# 1) Event Type Distribution
# -------------------------
event_counts = df["event_type"].value_counts()

plt.figure(figsize=(8, 5))
event_counts.plot(kind="bar")
plt.title("Event Type Distribution")
plt.xlabel("Event Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "event_type_distribution.png", dpi=300)
plt.close()

# -------------------------
# 2) Top 10 Categories by Events
# -------------------------
top_categories = (
    df["category_code"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))
top_categories.sort_values().plot(kind="barh")
plt.title("Top 10 Categories by Events")
plt.xlabel("Event Count")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "top_categories.png", dpi=300)
plt.close()

# -------------------------
# 3) Top 10 Brands by Revenue
# -------------------------
brand_revenue = (
    df[df["event_type"] == "purchase"]
    .groupby("brand")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
brand_revenue.sort_values().plot(kind="barh")
plt.title("Top 10 Brands by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Brand")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "top_brands_by_revenue.png", dpi=300)
plt.close()

# -------------------------
# 4) Daily Event Trend
# -------------------------
daily_events = df.groupby("date").size()

plt.figure(figsize=(12, 5))
daily_events.plot()
plt.title("Daily Event Trend")
plt.xlabel("Date")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "daily_event_trend.png", dpi=300)
plt.close()

# -------------------------
# 5) Revenue by Category
# -------------------------
category_revenue = (
    df[df["event_type"] == "purchase"]
    .groupby("category_code")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
category_revenue.sort_values().plot(kind="barh")
plt.title("Top 10 Categories by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "top_categories_by_revenue.png", dpi=300)
plt.close()

# -------------------------
# 6) Event Type Percentages
# -------------------------
event_pct = (event_counts / event_counts.sum()) * 100

plt.figure(figsize=(8, 5))
event_pct.plot(kind="pie", autopct="%1.2f%%", startangle=90)
plt.ylabel("")
plt.title("Event Type Share")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "event_type_share.png", dpi=300)
plt.close()

print("\nEDA complete.")
print("Charts saved in: ../images/")