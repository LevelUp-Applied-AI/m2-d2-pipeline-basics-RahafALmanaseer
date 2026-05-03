"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
   
    series = pd.Series([10, 20, np.nan, 30])
    result = clean_column(series)
    
    assert result.isna().sum() == 0
    assert result[2] == 20.0


def test_compute_revenue():
   
    quantity = pd.Series([2, 5, 10])
    price = pd.Series([10, 20, 5])
    
    result = compute_revenue(quantity, price)
    expected_result = pd.Series([20, 100, 50])
    
    pd.testing.assert_series_equal(result, expected_result)