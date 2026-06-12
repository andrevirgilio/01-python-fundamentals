import pandas as pd

df = pd.read_csv("vendas.csv")

print("Total vendido:", df["valor"].sum())
print("Venda média:", df["valor"].mean())
print("Maior venda:", df["valor"].max())
print("Menor venda:", df["valor"].min())