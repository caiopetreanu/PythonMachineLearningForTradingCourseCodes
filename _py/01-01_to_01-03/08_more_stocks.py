''' Build a dataframe in pandas '''

import pandas as pd

def run():

    # define date range
    startDate = '1993/01/29'
    endDate = '2017/06/24'
    dates = pd.date_range(startDate, endDate)

    # create an empry dataframe
    df1 = pd.DataFrame(index=dates)

    # read SPY datra into temporary dataframe
    dfSPY = pd.read_csv("C:/study/video/udacity/Machine_Learning_for_Trading/_data/SPY.csv",
                        index_col="Date",
                        parse_dates=True,
                        usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    # rename 'Adj Close' column to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close' : 'SPY'})

    # join the two dataframes using DataFrame.join
    df1 = df1.join(dfSPY, how="inner")

    # read in mor stocks
    symbols = ['GOOG', 'IBM', 'APPL', 'GLD']

    for symbol in symbols:

        dfTemp = pd.read_csv("C:/study/video/udacity/Machine_Learning_for_Trading/_data/{}.csv".format(symbol),
                             index_col="Date",
                             parse_dates=True,
                             usecols=['Date', 'Adj Close'],
                             na_values=['nan'])

        dfTemp = dfTemp.rename(columns={'Adj Close' : symbol})
        df1 = df1.join(dfTemp) # use default how = 'left'

    print(df1)

if __name__ == "__main__":
    run()