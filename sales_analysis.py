"""
Sales Data Analysis
Beginner-friendly project using pandas and matplotlib.
Run from the project folder: python sales_analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "sales_data.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    # Load the dataset
    df = pd.read_csv(DATA_FILE)

    # Basic data cleaning and preparation
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    numeric_columns = ["Quantity", "UnitPrice", "Discount"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df = df.dropna(subset=["OrderDate", "Region", "Product", "Quantity", "UnitPrice"])
    df = df.drop_duplicates()

    # Calculate revenue after discount
    df["GrossSales"] = df["Quantity"] * df["UnitPrice"]
    df["Revenue"] = df["GrossSales"] - (df["Quantity"] * df["Discount"])
    df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)

    # Summary metrics
    total_revenue = df["Revenue"].sum()
    total_orders = len(df)
    total_units = df["Quantity"].sum()
    average_order_value = total_revenue / total_orders if total_orders else 0

    print("\n=== SALES DATA ANALYSIS ===")
    print(f"Rows analyzed: {len(df)}")
    print(f"Total revenue: ₹{total_revenue:,.2f}")
    print(f"Orders (rows): {total_orders}")
    print(f"Units sold: {total_units:,.0f}")
    print(f"Average revenue per order row: ₹{average_order_value:,.2f}")

    product_summary = (
        df.groupby("Product", as_index=False)
          .agg(Revenue=("Revenue", "sum"), UnitsSold=("Quantity", "sum"))
          .sort_values("Revenue", ascending=False)
    )
    region_summary = df.groupby("Region", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False)
    monthly_summary = df.groupby("Month", as_index=False)["Revenue"].sum()

    product_summary.to_csv(OUTPUT_DIR / "product_summary.csv", index=False)
    region_summary.to_csv(OUTPUT_DIR / "region_summary.csv", index=False)
    monthly_summary.to_csv(OUTPUT_DIR / "monthly_summary.csv", index=False)

    print("\nRevenue by product:")
    print(product_summary.to_string(index=False))
    print("\nRevenue by region:")
    print(region_summary.to_string(index=False))

    # Chart 1: monthly revenue trend
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_summary["Month"], monthly_summary["Revenue"], marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue (₹)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150)
    plt.close()

    # Chart 2: revenue by product
    plt.figure(figsize=(9, 5))
    plt.bar(product_summary["Product"], product_summary["Revenue"])
    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue (₹)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_by_product.png", dpi=150)
    plt.close()

    # Chart 3: revenue by region
    plt.figure(figsize=(8, 5))
    plt.bar(region_summary["Region"], region_summary["Revenue"])
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue (₹)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_by_region.png", dpi=150)
    plt.close()

    print(f"\nSaved summary CSV files and charts in: {OUTPUT_DIR}")
    print("Analysis complete!")

if __name__ == "__main__":
    main()
