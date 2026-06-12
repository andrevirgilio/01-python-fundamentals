import pandas as pd

df = pd.read_csv("sales.csv")

print("\n=== ALL DATA ===")
print(df)

print("\n=== SALES IN AMERICANA ===")
print(df[df["cidade"] == "Americana"])

print("\n=== SALES GREATER THAN 150 ===")
print(df[df["valor"] > 150])

print("\n=== TOTAL SALES BY CITY ===")
print(df.groupby("cidade")["valor"].sum())