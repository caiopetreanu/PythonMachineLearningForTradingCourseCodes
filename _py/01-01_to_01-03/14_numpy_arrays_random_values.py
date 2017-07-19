""" Generating random numbers. """
import numpy
import numpy as np

def run():

    # generate an array full of random numbers, uniformly sampled from [0.0, 1.0)
    print("pass in a size tuple", np.random.random((5, 4))) # pass in a size tuple
    print("function arguments (not a tuple)", np.random.rand(5, 4))  # function arguments (not a tuple)

    # sample numbers from a Gaussian (normal) distribution
    print('"standard normal" (mean = 0, s.d. = 1)"', np.random.normal(size=(2, 3))) # "standard normal" (mean = 0, s.d. = 1)
    print('change mean to 50 and s.d. to 10', np.random.normal(50, 10, size=(2, 3)))  # change mean to 50 and s.d. to 10

    # random integers
    print("a single integer in [0, 10)", np.random.randint(10)) # a single integer in [0, 10)
    print("same as above, specifying [low, high) explicit", np.random.randint(0, 10))  # same as above, specifying [low, high) explicit
    print("5 random integers as a 1D array", np.random.randint(0, 10, size=5))  # 5 random integers as a 1D array
    print("2x3 array of random integers", np.random.randint(0, 10, size=(2, 3)))  # 2x3 array of random integers

if __name__ == "__main__":
    run()