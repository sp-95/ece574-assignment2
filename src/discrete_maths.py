import math
from typing import List


def mean(n: List[int | float]) -> float:
    return sum(n) / len(n)  # Calculate the average value


def variance(n: List[int | float]) -> float:
    """This is a function to calculate the variance in a list of numbers
    
    Parameters
    ----------
    n: list of int or float
        List of numbers
    
    Returns
    -------
    int or float
        Variance of the values in n
    """
    # Calculate the dataset mean
    x_avg = mean(n)

    # Calculate the square of the distance of each point from the mean value
    x_minus_x_avg__squared = [(x - x_avg)**2 for x in n]

    # Sum of those values
    numerator = sum(x_minus_x_avg__squared)

    # Divide by n - 1
    return numerator / (len(n) - 1)


def std_deviation(n: List[int | float]) -> float:
    return math.sqrt(variance(n))  # Calculate the standard deviation
