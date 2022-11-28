import math

import pandas as pd
import pytest

from src import calculus

data = pd.read_csv("data/Program 5A.csv")


@pytest.mark.parametrize(
    "test_input, expected",
    zip(data.x, data.Fx),
)
def test_standard_normal_distribution_derivative(test_input, expected):
    assert (
        round(calculus.standard_normal_distribution_derivative(test_input), 5)
        == expected
    )


@pytest.mark.parametrize(
    "x_low, x_high, expected",
    [
        (-math.inf, 2.5, 0.9938),
        (-math.inf, 0.2, 0.5793),
        (-math.inf, -1.1, 0.1357),
    ],
)
def test_integrate_standard_normal_distribution(x_low, x_high, expected):
    assert (
        round(
            calculus.integrate_standard_normal_distribution(x_low=x_low, x_high=x_high),
            4,
        )
        == expected
    )
