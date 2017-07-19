''' Daily portfolio value. '''

import matplotlib.pyplot as plt
import pandas as pd

from utils.util import get_data, plot_data, p, symbol_to_path, compute_daily_returns_numpy, compute_daily_returns_pandas, compute_cumulative_returns_pandas, normalize_data, compute_sharpe_ratio

""" 

1. Prices

2. Normed
    2.1 normed = prices/prices[0]

3. Alloced
    3.1 alloced = normed * allocs

4. Pos_Vals
    4.1 pos_vals = alloced * start_val

5. Port_Vals
    5.1 port_val = pos_vals.sum(axis=1)
 
"""

''' Portfolio statistics. '''

"""

    daily_rets = daily_rets[1:] # removes the firts day which will always be 0
    
    - cum_ret (cumulative return) = (port_val[-1] / port_val[0]) - 1
    - avg_daily_ret (average daily return) = daily_rets.mean()
    - std_daily_ret (s.d. of daily return) = daily_rets.std()
    - sharpe_ratio (rewards in the context of risk (s.d. or volatility))
        -> risk adjusted return
        -> all else being equal, lower risk or higher return is better
        -> sr also considers risk-free rate of return (like bank account or short-term treasury)
        -> in python:
            Sdaily = 252 ^ (1/2) * mean(daily_rets - daily_rf) / std(daily_rets - daily_rf) # daily_rf can be removed in divisor because it is a constant in s.d. and so it can be equal to 0
            Sweekly = 52 ^ (1/2) * mean(daily_rets - daily_rf) / std(daily_rets - daily_rf) # k = 52, is a constant based on frequency
            Smonthly = 12 ^ (1/2) * mean(daily_rets - daily_rf) / std(daily_rets - daily_rf)
        -> samples of used risk-free rate:
            - LIBOR
            - 3mo T-bill
            - 0(% - traditional shortcut)
            - daily_rf = ((1.0 + 0.1) ^ (1/252)) - 1 # 252 labor days, year rate of return of 10% (0.1)
                -> Super CDB (21,22% em 2 anos - impostos) = 0,00038189212949142526545790515766
                -> CDI (10,14% a.a.) = 0,0003833357474170823061957748799 - impostos
                -> Poupança (0,59% a.m. ~ 7,31% a.a.) = 0,0002801660562357370191865564328 - impostos
                -> Poupança (8,8 % a.a.) = 0,00033474311093464174105125034585 - impostos
                -> Tesouro IPCA+ 2024 (NTNB Princ) (5,54% a.a.) = 0,00021399051964761073592964909790 - impostos
                -> Tesouro Prefixado 2023 (LTN) (10,61% a.a.) = 0,00040024005455064452621568488331617 - impostos

"""

def run():

    # Read data
    dates = pd.date_range('2009-01-01', '2017-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)

    normed = normalize_data(df)
    p("normed", normed)

    allocs = [0.5, 0.2, 0.3]
    alloced = normed * allocs
    p("alloced", alloced)

    start_val = 1000000.00
    pos_vals = alloced * start_val
    p("pos_vals ", pos_vals )

    port_val = pos_vals.sum(axis=1)

    pd.set_option('display.float_format', lambda x: '%.6f' % x)
    pd.set_option('display.max_rows', len(port_val))

    p("port_val", port_val)

    cum_ret = compute_cumulative_returns_pandas(port_val)
    p("cum_ret", cum_ret)

    daily_rets = compute_daily_returns_pandas(df)

    avg_daily_ret = daily_rets.mean()
    p("avg_daily_ret", avg_daily_ret)

    std_daily_ret = daily_rets.std()
    p("std_daily_ret", std_daily_ret)

    compute_sharpe_ratio(daily_rets, 0.0, 252, "default")
    compute_sharpe_ratio(daily_rets, 0.00040024005455064452621568488331617, 252, "Tesouro Prefixado 2023 (LTN) (10,61% a.a.)")
    compute_sharpe_ratio(daily_rets, 0.0002801660562357370191865564328, 252, "Poupança (0,59% a.m.)")

    ''' "Usually, any Sharpe ratio greater than 1 is considered acceptable to good by investors. A ratio higher than 2 is rated as very good, and a ratio of 3 or higher is considered excellent. The basic purpose of the Sharpe ratio is to allow an investor to analyze how much greater a return he or she is obtaining in relation to the level of additional risk taken to generate that return." '''
    p("Usually, any Sharpe ratio greater than 1 is considered acceptable to good by investors.", "A ratio higher than 2 is rated as very good, and a ratio of 3 or higher is considered excellent.", "The basic purpose of the Sharpe ratio is to allow an investor to analyze how much greater\na return he or she is obtaining in relation to the level of additional risk taken to generate that return.")

    pd.reset_option('display.max_rows')
    pd.reset_option('display.float_format')

    df.plot()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run()