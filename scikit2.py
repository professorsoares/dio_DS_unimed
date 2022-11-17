from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import matplotlib .pyplot as plt


# gerando uma massa de dados:
x, y = make_regression(n_samples=200, n_features=1, noise=30)

# Plota os pontos gerados com a massa de dados.
plt.scatter(x, y)

# initialize & fit the model
modelo = LinearRegression().fit(x,y)

# now predict
plt.plot(x, modelo.predict(x), color='red', linewidth=3)
plt.show()


