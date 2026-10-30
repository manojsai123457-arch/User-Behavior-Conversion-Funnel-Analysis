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
print("Loading data for Funnel Analysis...")
print("=" * 60)

df = pd.read_csv(DATA_FILE)

# Clean / parse
df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")
df["brand"] = df["brand"].fillna("Unknown")
df["category_code"] = df["category_code"].fillna("Unknown")

print("Shape:", df.shape)

# -------------------------
# Session-level funnel
# -------------------------
session_order = (
    df.groupby("user_session")
    .agg(
        first_view_time=("event_time", lambda x: x[df.loc[x.index, "event_type"].eq("view")].min()),
        first_cart_time=("event_time", lambda x: x[df.loc[x.index, "event_type"].eq("cart")].min()),
        first_purchase_time=("event_time", lambda x: x[df.loc[x.index, "event_type"].eq("purchase")].min()),
    )
    .reset_index()
)

# Step counts
total_sessions = session_order["user_session"].nunique()
sessions_with_view = session_order["first_view_time"].notna().sum()

sessions_view_to_cart = (
    session_order["first_view_time"].notna()
    & session_order["first_cart_time"].notna()
    & (session_order["first_cart_time"] > session_order["first_view_time"])
).sum()

sessions_cart_to_purchase = (
    session_order["first_cart_time"].notna()
    & session_order["first_purchase_time"].notna()
    & (session_order["first_purchase_time"] > session_order["first_cart_time"])
).sum()

# Conversion rates
view_to_cart_rate = (sessions_view_to_cart / sessions_with_view * 100) if sessions_with_view else 0
cart_to_purchase_rate = (sessions_cart_to_purchase / sessions_view_to_cart * 100) if sessions_view_to_cart else 0
view_to_purchase_rate = (sessions_cart_to_purchase / sessions_with_view * 100) if sessions_with_view else 0

print("\nFunnel Summary")
print("-" * 60)
print("Total sessions:", total_sessions)
print("Sessions with view:", sessions_with_view)
print("Sessions view -> cart:", sessions_view_to_cart)
print("Sessions cart -> purchase:", sessions_cart_to_purchase)
print(f"View -> Cart Rate: {view_to_cart_rate:.2f}%")
print(f"Cart -> Purchase Rate: {cart_to_purchase_rate:.2f}%")
print(f"View -> Purchase Rate: {view_to_purchase_rate:.2f}%")

# Save summary
summary = pd.DataFrame({
    "step": ["Sessions", "View", "View -> Cart", "Cart -> Purchase"],
    "count": [total_sessions, sessions_with_view, sessions_view_to_cart, sessions_cart_to_purchase]
})
summary.to_csv("../reports/funnel_summary.csv", index=False)

# -------------------------
# Funnel chart
# -------------------------
plt.figure(figsize=(8, 5))
steps = ["Sessions", "View", "View -> Cart", "Cart -> Purchase"]
counts = [total_sessions, sessions_with_view, sessions_view_to_cart, sessions_cart_to_purchase]

plt.bar(steps, counts)
plt.title("User Funnel Analysis")
plt.xlabel("Funnel Step")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "funnel_analysis.png", dpi=300)
plt.close()

# -------------------------
# Event-type share chart
# -------------------------
event_counts = df["event_type"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(event_counts.values, labels=event_counts.index, autopct="%1.2f%%", startangle=90)
plt.title("Event Type Share")
plt.tight_layout()
plt.savefig(IMAGES_DIR / "event_type_share_funnel.png", dpi=300)
plt.close()

print("\nFunnel analysis complete.")
print("Charts saved in: ../images/")
print("Summary saved in: ../reports/funnel_summary.csv")