import pandas as pd
url = "https://raw.githubusercontent.com/muralimekala/python/master/Resp2.csv"
df_resp = pd.read_csv(url)

url = "https://raw.githubusercontent.com/muralimekala/python/master/Salaries.csv"
df_salarie = pd.read_csv(url)

print(df_salarie.head())
print(df_resp.shape)
print(df_salarie.columns)
print("Sal shape:", str(df_salarie.shape))
