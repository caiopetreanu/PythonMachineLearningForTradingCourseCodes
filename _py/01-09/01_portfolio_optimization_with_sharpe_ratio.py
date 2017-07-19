''' Fit a polynomial to a given set of data points using optimization. '''

import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

from utils.util import p, compute_sharpe_ratio, compute_daily_returns_numpy

"""

Framing the problem:

    1. provide a function to minimize f(x) - x are the allocations. But we want the max sharpe ration, not the min
    (solution: multiply s.r. by 1)
    2. provide an initial guess to x
    3. call the optimizer

Ranges and constraints:

    - ranges (makes optimizer runs faster): limits on values for x (between 0 and 1 is best, because 
    there is no 200% allocation of your funds)
    - constraints (essential for working): properties of x that must remain "true" (sum of 
    the allocations must add up to 1, using abs() - module/absolute function)

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import scipy.optimize as spo
import datetime as dt
from utils.util import compute_daily_returns_pandas

def symbol_to_path(symbol, base_dir="C:/study/video/udacity/Machine_Learning_for_Trading/_data/"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):

    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:

        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan', 'null'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)

        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df

def show_plot(dfcopy, df_alloc):

    # Plot portfolio along SPY
    dfcopynormed = dfcopy['SPY'] / dfcopy['SPY'].ix[0]
    ax = dfcopynormed.plot(title="Daily Portfolio ['SPY', 'APPL', 'XOM'] Value and SPY", label='SPY')
    sumcopy = dfcopy.sum(axis=1)
    normed = sumcopy / sumcopy.ix[0]
    normed.plot(label='Portfolio Value', ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')

    bx = dfcopy.plot(label='Stocks')
    bx.legend(loc='upper left')

    plt.show()

def find_portfolio_statistics(allocs, df, gen_plot):

    dfcopy = df.copy()

    # Find cumulative value over time
    df = (df/df.ix[0])
    df = df * allocs
    df = df.sum(axis=1)

    # Compute Portfolio Statistics
    cumulative_return = (df.ix[-1]/df.ix[0]) - 1

    dailyreturns = (df.ix[1:]/df.ix[:-1].values) - 1

    average_daily_return = dailyreturns.mean(axis=0)
    std_daily_return = dailyreturns.std(axis=0)

    sharpe_ratio = compute_sharpe_ratio(dailyreturns, 0.00040024005455064452621568488331617, 252, "Portfolio optimization agaist Tesouro Prefixado 2023 (LTN) (10,61% a.a.)")
    # sharpe_ratio = (252**(1/2.0)) * ((average_daily_return-0)/std_daily_return)

    ending_value = df.ix[-1]
    total_returns = average_daily_return*(252/252)

    if gen_plot == True:
        show_plot(dfcopy, dfcopy.sum(axis=1))

    return (-1 * sharpe_ratio)

def optimize_allocations(sd, ed, symbols, gen_plot):

    dates = pd.date_range(pd.to_datetime(sd), pd.to_datetime(ed))
    df = get_data(symbols, dates)

    initial_guess = []
    bounds = ()
    l = list(bounds)
    for column in df:
        initial_guess.append(1/float(df.shape[1]))
        l.append((0.0,1.0))

    max_result = spo.minimize(find_portfolio_statistics, np.float32(initial_guess), args=(df, gen_plot,),method='SLSQP',bounds=tuple(l))
    print(' Recomended allocations for {}: {}'.format(symbols, max_result.x))

    dfcopy = df.copy()
    df_alloc = df * max_result.x

    df_up = df_alloc.sum(axis=1)

    cumulative_return = (df_up.ix[-1]/df_up.ix[0]) - 1
    dailyreturns = (df_up.ix[1:]/df_up.ix[:-1].values) - 1
    average_daily_return = dailyreturns.mean(axis=0)
    std_daily_return = dailyreturns.std(axis=0)

    sharpe = find_portfolio_statistics(max_result.x, df, True) * -1

    print('\n Cumulative Return: {}\n'.format(cumulative_return),
      'Average Daily Return: {}\n'.format(average_daily_return),
      'Standard Deviation of Daily Returns: {}\n'.format(std_daily_return),
      'Sharpe Ratio: {}\n'.format(sharpe))

    if gen_plot == True:
        show_plot(dfcopy, df_alloc)

if __name__ == "__main__":
    optimize_allocations('2016-04-26', '2017-03-19', ['SPY', 'APPL', 'XOM'], False)