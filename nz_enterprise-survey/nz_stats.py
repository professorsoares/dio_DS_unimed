
# NZ -> New Zealand DATA:
# https://www.stats.govt.nz/information-releases/annual-enterprise-survey-2021-financial-year-provisional

# STATS Website:
# https://www.stats.govt.nz/publications?filters=New%20Zealand%20business%20demography%20statistics%2CInformation%20releases

from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import matplotlib .pyplot as plt
import pandas as pd

url = "annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
df_resp = pd.read_csv(url)

print(df_resp)
print("-----------------------------------")
print(df_resp.duplicated())
print("-----------------------------------")
print(df_resp[df_resp.duplicated()])
print("-----------------------------------")
print(df_resp.columns)
print("-----------------------------------")
print(df_resp["Industry_code_ANZSIC06"].unique())

# # gerando uma massa de dados:
# x, y = make_regression(n_samples=200, n_features=1, noise=30)
#
# # Plota os pontos gerados com a massa de dados.
# plt.scatter(x, y)
#
# # initialize & fit the model
# modelo = LinearRegression().fit(x,y)
#
# # now predict
# plt.plot(x, modelo.predict(x), color='red', linewidth=3)
# plt.show()
#
#
