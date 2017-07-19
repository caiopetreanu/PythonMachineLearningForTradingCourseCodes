""" Array attributes. """

import numpy as np

def run():

    a = np.random.random((5, 4)) # 5x4 array of random numbers
    print("number of rows", a.shape[0]) # number of rows
    print("number of columns", a.shape[1])  # number of columns
    print("lenght", len(a.shape))
    print("size", a.size)
    print("a", a)
    print("dtype", a.dtype)

if __name__ == "__main__":
    run()