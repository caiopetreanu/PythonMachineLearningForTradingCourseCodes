''' Build a dataframe in pandas '''

import pandas as pd
import os
import matplotlib.pyplot as plt

""" Utility functions """

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
    ax = df.plot(title = title, fontsize = 2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    plt.show() # must be called to show plots in some environments

def run():

    # define a date range
    dates = pd.date_range('1930-01-01', '2017-06-24')

    # choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD', 'APPL'] # SPY will be added in get_data()

    # get stock data
    df = get_data(symbols, dates)

    # slice by row range (dates) using DataFrame.ix[] selector
    #print(df.ix['2010-01-01' : '2010-01-31']) # the month of January

    # slice by column (symbols)
    #print(df['GOOG']) # a single label selects a single column
    #print(df[['IBM', 'GLD']]) # a list of labels selects multiple columns

    # slice by row and column
    #print(df.ix['2010-03-10' : '2010-03-15', ['SPY', 'IBM']])

    #plot_data(df, 'Stock Prices')
    #plot_data(df.ix['2010-03-10' : '2010-03-15', ['SPY', 'IBM']], 'Stock Prices')

    plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')

if __name__ == "__main__":
    run()