''' Scatterplots in python. '''

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
import numpy as np

from utils.util import get_data,\
    plot_data,\
    p,\
    symbol_to_path,\
    compute_daily_returns_numpy,\
    compute_daily_returns_pandas,\
    compute_cumulative_returns_pandas

def run():

    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)
    # plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns_pandas(df)
    # plot_data(daily_returns, title="Daily Returns", ylabel="Daily Returns")

    # polynomial of degree 1. Returns a (beta, slope) and b (alpha, where axis y is intercepted) from formulae: y = ax + b
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter', x='SPY', y='XOM', color='w', edgecolor="r", linewidth=1,
                       title='SPY x XOM Scatterplot (higher slope, higher correlation ({:.6f}), {:.6f}x + {:.6f})'.format(
                           daily_returns.corr(method='pearson')['SPY']['XOM'], beta_XOM, alpha_XOM), fontsize=12)

    plt.grid(True)
    plt.plot(daily_returns['SPY'], beta_XOM * daily_returns['SPY'] + alpha_XOM, '-', color='blue')

    # polynomial of degree 1. Returns a (beta, slope) and b (alpha, where axis y is intercepted) from formulae: y = ax + b
    beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)

    # Scatterplot SPY vs GLD
    daily_returns.plot(kind='scatter', x='SPY', y='GLD', color='w', edgecolor="y", linewidth=1,
                       title='SPY x GLD Scatterplot (lower slope, lower correlation ({:.6f}), {:.6f}x + {:.6f})'.format(
                           daily_returns.corr(method='pearson')['SPY']['GLD'], beta_GLD, alpha_GLD),
                       fontsize=12)

    plt.grid(True)
    plt.plot(daily_returns['GLD'], beta_GLD * daily_returns['GLD'] + alpha_GLD, '-', color='green')

    p()

    # Compute and plot both histograms on the same chart
    # daily_returns['SPY'].hist(bins=20, label='SPY', color='yellow', edgecolor="black", linewidth=2)
    # daily_returns['XOM'].hist(bins=20, label='XOM', color='red', edgecolor="black", linewidth=2)
    # plt.legend(loc='upper right')

    # Plot a histogram
    # n = daily_returns.hist(color='yellow', edgecolor="black", linewidth=2) # changing no. of bins from 10 to 20

    # # Get mean and standard deviation
    # mean = daily_returns['SPY'].mean()
    # p("Mean = ", mean)
    # std = daily_returns['SPY'].std()
    # p('STD = ', std)
    #
    # plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    # plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    # plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    #
    # fig, ax = plt.subplots()
    # p(daily_returns['SPY'].values)
    # n, bins, patches = ax.hist(daily_returns['SPY'].values, 20, color='yellow', edgecolor="black", linewidth=2)
    # y = mlab.normpdf(bins, mean, std)
    # ax.plot(bins, y, '--')
    #
    # ax.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    # ax.axvline(std, color='r', linestyle='dashed', linewidth=2)
    # ax.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    #
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Price')
    #
    # # Compute kurtosis
    # kurtosis = daily_returns.kurtosis().values
    # ax.set_title(r'Histograma: $\mu=[{}]$, $\sigma=[{}]$, $kurtosis={}$'.format(mean, std, kurtosis))
    # plt.xticks(bins)

    plt.show()

if __name__ == "__main__":
    run()