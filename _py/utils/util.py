''' Plot a histogram. '''

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

""" Utility functions """

def p(*args):
    print("\n")
    for arg in args:
        print(arg)

def symbol_to_path(symbol, baseDir = "C:/study/video/udacity/Machine_Learning_for_Trading/_data/"):

    """ Return CSV file path given a ticker symbol. """
    return os.path.join(baseDir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):

    """ Read stock data (adjusted close) for given symbols from CSV files. """
    df = pd.DataFrame(index = dates)

    if 'SPY' not in symbols: # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:

        dfTemp = pd.read_csv(symbol_to_path(symbol),
                             index_col="Date",
                             parse_dates=True,
                             usecols=['Date', 'Adj Close'],
                             na_values=['nan'])

        dfTemp = dfTemp.rename(columns={'Adj Close' : symbol})
        df = df.join(dfTemp)

        if symbol == 'SPY': # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df

def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.grid(True)

def compute_daily_returns_numpy(df):
    """ Compute and return daily return values. """

    daily_returns = df.copy() # copy given DataFrame to match size and column names

    # compute daily returns for row 1 onwards
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0

    # Note: Returned DataFrame musta have the same number of rows
    return daily_returns

def compute_daily_returns_pandas(df):
    """ Compute and return daily return values. """
    daily_returns = (df / df.shift(1)) - 1 # much easier with Pandas!
    daily_returns.ix[0, :] = 0  # Pandas leaves the 0th row full of NaNs
    return daily_returns

def compute_cumulative_returns_pandas(df):
    """ Compute and return cumulative return values. """
    cumulative_returns = (df / df.ix[0, :]) - 1
    return cumulative_returns

def normalize_data(df):
    """ normalize stock prices using the first row of the dataframe. """
    return df/df.ix[0,:]

def compute_sharpe_ratio(daily_rets, daily_rf, year_frequency, title):
    k = np.sqrt(year_frequency)
    sharpe_ratio = k * ((daily_rets - daily_rf).mean() / (daily_rets - daily_rf).std())
    #p(title, "sharpe_ratio (daily_rf = {})".format(daily_rf), sharpe_ratio)
    return sharpe_ratio