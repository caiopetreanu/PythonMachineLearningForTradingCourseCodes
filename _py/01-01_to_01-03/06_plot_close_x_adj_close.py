# 06

"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt


def run_test():
    df = pd.read_csv("C:/study/video/udacity/Machine_Learning_for_Trading/_data/APPL.csv")
    df[['Close', 'Adj Close']].plot()
    plt.xlabel('Close')
    plt.ylabel('Adj Close')
    plt.title('APPL Historic Closing')
    plt.grid(True)
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    run_test()