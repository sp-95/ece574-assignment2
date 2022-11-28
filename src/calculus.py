"""
Program Assignment:     5A
Name:                   Shashanka Prajapati
Date:                   
Description:            Program to numerically integrate a function

Table of Contents:
    integrate(
        x_low: int,
        x_high: int,
        number_of_segments: int,
        error_margin: float,
        old_result: Optional[float] = 0.0,
    ) -> float
"""

import math
from typing import Callable, Optional

import numpy as np


def integrate(
    function: Callable[[int | float], float],
    x_low: int,
    x_high: int,
    number_of_segments: int,
    error_margin: float,
    old_result: Optional[float] = 0.0,
) -> float:
    """To evaluate the integral of a known function F(x) between two given points

    Parameters
    ----------
    function: Callable[[int | float], float]
        function F(x) whose integral is to be evaluated
    x_low : int
        lower integration limit
    x_high : int
        upper integration limit
    number_of_segments : int
        number of segments in the integration
    error_margin : float
        acceptable error of the result
    old_result : Optional[float], optional
        the previous answer, by default 0.0

    Returns
    -------
    float
        The integration result
    """
    # Calculate the width of each segment
    width = (x_high - x_low) / number_of_segments

    # Compute the integral value
    result = 0
    for i, x in enumerate(np.arange(x_low, x_high + width, width)):
        # print(f"Term number i = {i}")
        # print(f"x{i} = {x}")
        if i == 0 or i == number_of_segments:
            term = function(x)
        elif i % 2 == 1:
            term = 4 * function(x)
        else:
            term = 2 * function(x)
        term *= width / 3
        # print(f"Term({i}) = {round(term, 6)}")

        result += term

    # Compare the result against the acceptable error
    if abs(result - old_result) <= error_margin:
        return result

    # Adjust the parameter values and calculate again
    return integrate(
        function=function,
        x_low=x_low,
        x_high=x_high,
        number_of_segments=2 * number_of_segments,
        error_margin=error_margin,
        old_result=result,
    )


def standard_normal_distribution_derivative(x: int | float) -> float:
    """Compute the value of the first derivative of standard normal distribution
    at point x

    Parameters
    ----------
    x : int | float
        A point in the standard normal distribution

    Returns
    -------
    float
        The value of the first derivative of standard normal distribution at point x
    """
    # Compute the value of the numerator
    power = x**2 / 2
    # print(f"(x^2) / 2 = {power}")
    numerator = math.exp(-power)
    # print(f"e^(-(x^2) / 2) = {numerator}")

    # Compute the value of the denominator
    denominator = math.sqrt(2 * math.pi)

    result = numerator / denominator
    # print(f"F(x) = {result}")
    return result


def integrate_standard_normal_distribution(
    x_low: int | float, x_high: int | float
) -> float:
    """Evaluate the integral value of a standard normal distribution
    from x_low to x_high

    Parameters
    ----------
    x_low : int | float
        The lower integration limit
    x_high : int | float
        The higher integration limit

    Returns
    -------
    float
        The integral value of the standard normal distribution from x_low to x_high
    """
    # Handle infinite cases as they cannot be handled by the integrate function
    # Handle the case for negative infinity
    if x_low == -math.inf:
        # If high is also infinity then it covers the whole range
        if x_high == math.inf:
            return 1
        # If high is exactly 0 then it covers half the area
        if x_high == 0:
            return 0.5
        # If both the points are in the same side of the mean
        if x_high < 0:
            return 0.5 - integrate(
                function=standard_normal_distribution_derivative,
                x_low=x_high,
                x_high=0,
                number_of_segments=20,
                error_margin=1e-4,
            )
        # If the points are in the opposite side of the mean
        if x_high > 0:
            return 0.5 + integrate(
                function=standard_normal_distribution_derivative,
                x_low=0,
                x_high=x_high,
                number_of_segments=20,
                error_margin=1e-4,
            )

    # Handle the case for infinity
    if x_high == math.inf:
        # If low is exactly 0 then it covers half the area
        if x_low == 0:
            return 0.5
        # If both the points are in the same side of the mean
        if x_low > 0:
            return 0.5 - integrate(
                function=standard_normal_distribution_derivative,
                x_low=0,
                x_high=x_low,
                number_of_segments=20,
                error_margin=1e-4,
            )
        # If the points are in the opposite side of the mean
        if x_low < 0:
            return 0.5 + integrate(
                function=standard_normal_distribution_derivative,
                x_low=x_low,
                x_high=0,
                number_of_segments=20,
                error_margin=1e-4,
            )


if __name__ == "__main__":
    # Probability values of the normal distribution integral from -∞ to 2.5
    print(integrate_standard_normal_distribution(x_low=-math.inf, x_high=2.5))

    # Probability values of the normal distribution integral from -∞ to 0.2
    print(integrate_standard_normal_distribution(x_low=-math.inf, x_high=0.2))

    # Probability values of the normal distribution integral from -∞ to -1.1
    print(integrate_standard_normal_distribution(x_low=-math.inf, x_high=-1.1))
