# 05

"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt


def run_test():
    df = pd.read_csv("C:/study/video/udacity/Machine_Learning_for_Trading/_data/IBM.csv")
    df['High'].plot()
    plt.xlabel('Inverse Time Series')
    plt.ylabel('Stock Highs')
    plt.title('IBM Highs')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    # plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    run_test()