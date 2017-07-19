""" Accessing array elements. """

import numpy as np
import numpy.ma as ma

def p(*args):
    print("\n")
    for arg in args:
        print(arg)

def run():

    a = np.random.rand(5, 4)
    p("Array:", a)

    # accessing element at postion (3, 2)
    element = a[3, 2]
    p("Element (3,2):", element)

    # elements in defined range
    p("Elements in defined range", a[0, 1:3])

    # top-leaf corner
    p("Top-left corner", a[0:2, 0:2])

    # note: Slice n:m:t specifies a range that starts at n, and stops before m, in steps of size t
    p("Note: Slice n:m:t specifies a range that starts at n, and stops before m, in steps of size t", a[:, 0:3:2]) # will select columns 0, 2 for every row

    # assigning a value to a particular location
    a[0, 0] = 1
    p("Modified (replaced one element):", a)

    # assigning a value to an entire row
    a[1, :] = 2
    p("Modified (replaced a row with a single value):", a)

    # assigning a list to a column in an array
    a[:, 3] = [1, 2, 3, 4, 5]
    p("Modified (replaced a column with a list:", a)

    a = np.random.rand(5)
    p("New a:", a)

    # accessing using list of indices
    indices = np.array([1,1,2,3])
    p("Accessing a with indices", indices, "Results in:", a[indices])

    a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    p("New a:", a)

    # calculating mean
    mean = a.mean()
    p("Mean:", mean)

    # masking
    p("Masking only values lower than the mean:", a[a < mean])
    p("Masking only values greater than the mean:", a[a > mean])

    p("Masking only values inside s.d. 3 according to the mean:", ma.masked_outside(a, mean-3, mean+3))
    p("Masking only values outside s.d. 3 according to the mean:", ma.masked_inside(a, mean - 3, mean + 3))

    p("Masking only values inside s.d. 5 according to the mean:", ma.masked_outside(a, mean - 5, mean + 5))
    p("Masking only values outside s.d. 5 according to the mean:", ma.masked_inside(a, mean - 5, mean + 5))

    p("Masking only values inside s.d. 10 according to the mean:", ma.masked_outside(a, mean - 10, mean + 10))
    p("Masking only values outside s.d. 10 according to the mean:", ma.masked_inside(a, mean - 10, mean + 10))

    a[a < mean] = mean
    p("Substitution by the mean value for only values lower than the mean:", a)


if __name__ == "__main__":
    run()