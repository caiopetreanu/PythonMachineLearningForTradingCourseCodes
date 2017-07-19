import pandas as pd

def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("C:/study/video/udacity/Machine_Learning_for_Trading/_data/{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()

def run_rest():
    """Function called by Test Run."""
    for symbol in ['AAPL', 'IBM']:
        print("Mean Volume")
        print(symbol, get_mean_volume(symbol))


if __name__ == "__main__":
    run_rest()