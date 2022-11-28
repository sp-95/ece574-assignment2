import pandas as pd
import pytest

from src.discrete_maths import mean, std_deviation

data = pd.read_csv("data/Program 1A.csv")


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (data.get("Object LOC", []), 550.60),
        (data.get("New and Changed LOC", []), 638.90),
        (data.get("Development Hours", []), 60.32),
    ],
)
def test_mean(test_input, expected):
    assert round(mean(test_input), 2) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (data.get("Object LOC", []), 572.03),
        (data.get("New and Changed LOC", []), 625.63),
        (data.get("Development Hours", []), 62.26),
    ],
)
def test_std_deviation(test_input, expected):
    assert round(std_deviation(test_input), 2) == expected
