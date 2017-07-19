''' Fit a polynomial to a given set of data points using optimization. '''

import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

from utils.util import p

def fit_poly(data, error_func, degree):

    """ Fit a polynomial to given data, using supplied error function.

    Parameters
    ----------
    data: 2D array where each row is a point (X0, Y)
    error_func: function that computes the error between a polynomial and observed data

    Returns polynomial that minimizes the error function
    """

    # Generate initial guess for polynomial model (all coeaffs = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))

    # Plot initial guess (optional)
    x = np.linspace(-6, 6, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label='Initial guess')

    # Call optimizer to minimize error function
    result = spo.minimize(error_func, Cguess, args=(data,), method="SLSQP", options={'disp': False})
    return np.poly1d(result.x) # convert optimal result into a poly1d and return


def error_poly(C, data):

    """ Compute error between given polynomial and observed data.

    Parameters
    ----------
    C: numpy.poly1d object or equivalent array representing polynomioal coeficients
    data: 2D array where each row is a point (x, y)

    Returns error as a single real value
    """

    # Metric: Sum of squared Y-axis differences
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2) # using sum()
    #err = np.sum(np.power((data[:, 1] - np.polyval(C, data[:, 0])), 2))  # using sum() and np.power()
    #err = np.mean((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)  # using mean()
    #err = np.mean(np.power((data[:, 1] - np.polyval(C, data[:, 0])), 2))  # using mean() and np.power()

    return err

def run():

    # Define original line
    #l_orig = np.float32([1.5, -10, -5, 60, 50])
    #l_orig = np.float32([1.7, 10, -14, 13, 110])
    l_orig = np.float32([5.1, 3, -1, 3, -10])
    p("Original line:\n\n{}".format(np.poly1d(l_orig)))

    Xorig = np.linspace(-6, 6, 21)
    Yorig = l_orig[0]*np.power(Xorig, 4) + l_orig[1]*np.power(Xorig, 3) + l_orig[2]*np.power(Xorig, 2) + l_orig[3]*Xorig + l_orig[4]
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label='Original line')

    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.array([Xorig, Yorig + noise]).T
    plt.plot(data[:,0], data[:,1], 'go', label='Data points')

    # Try to fit a line to this data
    l_fit = fit_poly(data, error_poly, 4)

    p("Fitted line:\n{}".format(l_fit))
    Xfit = data[:,0]
    Yfit = l_fit[4]*np.power(Xfit, 4) + l_fit[3]*np.power(Xfit, 3) + l_fit[2]*np.power(Xfit, 2) + l_fit[1]*Xfit + l_orig[0]
    plt.plot(Xfit, Yfit, 'r--', linewidth=2.0, label='Fitted line')

    # Add a legend and show plot
    plt.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    run()