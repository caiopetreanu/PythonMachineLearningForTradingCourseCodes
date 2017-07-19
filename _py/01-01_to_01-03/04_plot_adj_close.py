# 04

import pandas as pd
import matplotlib.pyplot as plt


def run_test():
    df = pd.read_csv("C:/study/video/udacity/Machine_Learning_for_Trading/_data/APPL.csv")
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    run_test()