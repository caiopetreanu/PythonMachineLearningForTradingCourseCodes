''' Computing rolling statistics. '''

import pandas as pd
import os
import matplotlib.pyplot as plt

""" Utility functions """

def p(*args):
    print("\n")
    for arg in args:
        print(arg)

def plot_selected(df, columns, start_index, end_index):

    """ plot the desired columns over index values in the given range."""
    plot_data(df.ix[start_index : end_index, columns], 'Selected Data')

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

def plot_data(df, title):

    ''' plot stock prices '''

    # option 1
    #df.plot()
    #plt.xlabel('Date')
    #plt.ylabel('Price')
    #plt.title('Stock Prices')

    # option 2
    ax = df.plot(title = title, fontsize = 20)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.grid(True)
    #plt.xticks(df.index, rotation=90)

    plt.show() # must be called to show plots in some environments

def run():

    # read data
    #dates = pd.date_range('2010-01-01', '2012-12-31')
    dates = pd.date_range('2012-01-01', '2012-12-31')

    symbols = ['SPY']
    df = get_data(symbols, dates)

    # plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY rolling mean", label="SPY")

    # compute the rolling mean using a 20-day window

    #rm_SPY = pd.rolling_mean(df['SPY'], window=20) # deprecated
    rm_SPY = pd.DataFrame.rolling(df['SPY'], window=20,center=False).mean() # new version of rolling mean for python 3

    rm_SPY.plot(label='Rolling mean', ax=ax)

    # add axis labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')

    plt.show()

if __name__ == "__main__":
    run()