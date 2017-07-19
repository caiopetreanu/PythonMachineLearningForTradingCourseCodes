""" Arithmetic operations. """

import numpy as np

def p(*args):
    print("\n")
    for arg in args:
        print(arg)

def run():

    a = np.array([(1,2,3,4,5),(1,20,30,40,50)])
    p("Original array a:", a)

    # multiply a by 2
    p("Multiply a by 2:", 2*a)

    # divide a by 2
    p("Divide a by 2:", a/2.0)

    b = np.array([(100,200,300,400,500),(1,2,3,4,5)])
    p("Original array b:", a)

    # add the two arrays
    p("Add a + b", a+b)

    # multiply a * b
    p("Multipy (element-wise, a.k.a. scalar multiplication) a times b", a * b)

    # divide a / b
    p("Divide (element-wise, a.k.a. scalar division) a by b", a / b)

if __name__ == "__main__":
    run()