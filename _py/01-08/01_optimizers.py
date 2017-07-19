''' What is an optimizer? '''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

from utils.util import p

""" 

Optimizers:

    - find minimum values of functions
    - build parameterized models based on data
    - refine allocations to stocks in portfolios
    
To use an optimizer:

    1. provide a function to minimize
    2. provide an initial guess
    3. call the optimizer

"""

def f(X):

    """ Given a scalar X, return some value (a real number) """
    Y = (X - 1.5)**2 + 0.5
    p("X = {}, Y = {}".format(X, Y)) # for tracing
    return Y

def run():

    Xguess = 2.0
    min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp': True})
    p("Minima found at", "X = {}, Y = {}".format(min_result.x, min_result.fun))

    # Plot function values, mark minima
    Xplot = np.linspace(0.5, 2.5, 21)
    Yplot = f(Xplot)
    plt.plot(Xplot, Yplot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.title("Minima of an objective function")
    plt.show()

if __name__ == "__main__":
    run()