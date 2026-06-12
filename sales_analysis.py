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

print("\n=== SORT BY SALES DESC ===")
print(df.sort_values("valor", ascending=False))

print("\n=== SALES WITH COMMISSION ===")
df["commission"] = df["valor"] * 0.10
print(df)

print("\n=== NULL VALUES ===")
print(df.isnull().sum())

print("\n=== CLEAN DATA ===")
clean_df = df.dropna()
print(clean_df)

result = (df.groupby("cidade")
            .agg(total_sales  = ("valor", "sum"),
                 max_sale     = ("valor", "max"),
                 min_sale     = ("valor", "min")
      )
);

print(result)