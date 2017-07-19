""" Creating NumPy arrays. """
import numpy
import numpy as np

def run():

    # list to 1D array
    print("list to 1D array", np.array([2, 3, 4]))

    # list of tuples to 2D array
    print("list of tuples to 2D array", np.array([(2, 3, 4), (5, 6, 7)]))

    # empty array
    print("empty array", np.empty(5))
    print("empty array", np.empty((5, 4)))
    print("empty array", np.empty((5, 4, 3)))

    # array of ones (float=default)
    print("array of ones (float=default)", np.ones((5, 4)))

    # array of ones (integer -127 to 128)
    print("array of ones (integer -127 to 128)", np.ones((5, 4), dtype=np.int8))

    # array of ones (integer)
    print("array of ones (integer)", np.ones((5, 4), dtype=np.int_))

if __name__ == "__main__":
    run()