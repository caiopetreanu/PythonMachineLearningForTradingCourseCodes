""" Using time function. """
""" How fast is NumPy? """

import numpy as np
import time
from time import time as t

def how_long(func, *args):

    """ Execute function with given arguments, and measure execution time. """
    t0 = t()

    result = func(*args) # all arguments are passed in as-is
    t1 = t()

    return result, t1 - t0

def manual_mean(arr):

    """ Compute mean (average) of all elements in the given 2D array. """
    sum = 0

    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            sum = sum + arr[i, j]

    return sum / arr.size

def numpy_mean(arr):
    """ Compute mean (average) using NumPy. """
    return arr.mean()

def run():

    p = print

    t1 = time.time()
    p("ML4T")

    t2 = time.time()
    p('The time taken to print statement is', t2 - t1, 'seconds')

    nd1 = np.random.random((1000, 10000)) # use a sufficiently large array

    # Time the two functions, retrieving results and execution times
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    p("Manual: {:.6f} ({:.3f} secs) vs. NumPy: {:.6f} ({:.3f} secs)".format(res_manual, t_manual, res_numpy, t_numpy))

    # Make sure both give us the same answer (upt some precision)
    assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal!"

    # Compute speedup
    speedup = t_manual / t_numpy
    p("NumPy mean is", speedup, "times faster than manual for loops.")


if __name__ == "__main__":
    run()