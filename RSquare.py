import numpy as np
import math

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE

    ymean = np.mean(data)
    num = 0
    den=0
    den = ((data-ymean)**2).sum()
    num = ((data-predictions)**2).sum()
    r_squared = 1 - (num/den)
    return r_squared
