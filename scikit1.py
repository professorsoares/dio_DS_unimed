from sklearn.datasets import make_regression
import matplotlib .pyplot as plt

def main(name):

    # gerando uma massa de dados:
    x, y = make_regression(n_samples=200, n_features=1, noise=30)
    plt.scatter(x, y)
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

