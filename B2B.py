import pandas as pd
import matplotlib.pyplot as plt

# Define file paths
base_path = r"C:\Users\basum\OneDrive\Documents\Downloads\Downloads\archive"
datasets = {
    "pincode_zones": f"{base_path}\\Company ABC - Pincode Zones.csv",
    "sku_master": f"{base_path}\\Company ABC - SKU Master.csv",
    "order_report": f"{base_path}\\Company ABC- Order Report.csv",
    "courier_rates": f"{base_path}\\Courier Company - Rates.csv",
    "courier_invoice": f"{base_path}\\Courier Company - Invoice.csv"
}

# Load datasets
df_pincode = pd.read_csv(datasets["pincode_zones"])
df_sku = pd.read_csv(datasets["sku_master"])
df_order = pd.read_csv(datasets["order_report"])
df_rates = pd.read_csv(datasets["courier_rates"])
df_invoice = pd.read_csv(datasets["courier_invoice"])

# Pincode Zone Analysis
zone_counts = df_pincode["Zone"].value_counts()
zone_counts.to_csv(f"{base_path}\\zone_analysis.csv", index=True)

# SKU Master Analysis
sku_counts = df_sku["SKU"].value_counts()
weight_stats = df_sku["Weight (g)"].describe()
sku_counts.to_csv(f"{base_path}\\sku_analysis.csv", index=True)

# Order Report Analysis
sku_order_qty = df_order.groupby("SKU")["Order Qty"].sum().sort_values(ascending=False)
sku_order_qty.to_csv(f"{base_path}\\order_analysis.csv", index=True)

# Courier Rates Analysis
forward_fixed_avg = df_rates.iloc[0, :5].mean()
forward_additional_avg = df_rates.iloc[0, 5:10].mean()
return_fixed_avg = df_rates.iloc[0, 10:15].mean()
return_additional_avg = df_rates.iloc[0, 15:].mean()
df_rate_summary = pd.DataFrame({
    "Category": ["Forward Fixed", "Forward Additional", "Return Fixed", "Return Additional"],
    "Average Cost": [forward_fixed_avg, forward_additional_avg, return_fixed_avg, return_additional_avg]
})
df_rate_summary.to_csv(f"{base_path}\\rate_analysis.csv", index=False)

# Courier Invoice Analysis (NEW)
zone_billing = df_invoice.groupby("Zone")["Billing Amount (Rs.)"].sum().sort_values(ascending=False)
zone_billing.to_csv(f"{base_path}\\invoice_analysis.csv", index=True)

# Visualization - SKU Order Distribution
plt.figure(figsize=(10, 5))
plt.bar(sku_order_qty.index[:10], sku_order_qty.values[:10], color="skyblue")
plt.xlabel("SKU")
plt.ylabel("Total Order Quantity")
plt.title("Top 10 SKU Order Distribution")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Visualization - Zone Billing Amount
plt.figure(figsize=(10, 5))
plt.bar(zone_billing.index, zone_billing.values, color="green")
plt.xlabel("Zone")
plt.ylabel("Total Billing Amount (Rs.)")
plt.title("Billing Amount per Zone")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

print("Analysis complete! Files saved in the archive folder.")
