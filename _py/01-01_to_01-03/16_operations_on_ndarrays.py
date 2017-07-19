""" Operations on arrays. """

import numpy as np

def get_max_index(a):

    """ Return the index of the maximum value in given 1D array. """
    return a.argmax()

def run():

    np.random.seed(693) # seed the ran dom number generator
    a = np.random.randint(0, 10, size=(5, 4)) # 5x4 random integers in [0, 10)
    print("Array :\n", a)

    # Sum of all elements
    print("Sum of all elements:", a.sum())

    # Iterate over rows, to compute sum of each column
    print("Sum of each column:\n", a.sum(axis=0))

    # Iterate over columns to compute sum of each row
    print("Sum of each row:\n", a.sum(axis=1))

    # Statistics: min, max, mean (across rows, column and overall)
    print("Minimum of each column:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.max(axis=1))
    print("Mean of all elements:\n", a.mean()) # leave out axis arg

    # print(np.asmatrix(a.max(axis=1)).T)
    # print(np.asmatrix(a.max(axis=1)).transpose())

    a = np.random.randint(0, 100, size=(10, 10))
    print("New matrix:\n", a)

    print("np.unravel_index() = argmax in a matrix:\n", np.unravel_index(a.argmax(), a.shape))
    x = np.unravel_index(a.argmax(), a.shape)[0]
    y = np.unravel_index(a.argmax(), a.shape)[1]
    print("unravel_index() =", a[x, y], ". a.max() =", a.max(), ". Are they equal?", a[x, y] == a.max())

    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print("Array:", a)

    # Find the maximum and its index in array
    print("Maximum value:", a.max())
    print("Index of max.:", get_max_index(a))

if __name__ == "__main__":
    run()