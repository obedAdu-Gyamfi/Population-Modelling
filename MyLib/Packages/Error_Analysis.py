#!/usr/bin/env python3
"""
This module provides functions for calculating various error metrics
"""

import numpy as np


def MSE(data1=None, data2=None):
    if data1 is None or data2 is None:
        raise ValueError("Data cannot be None")
    return np.mean((data1 - data2) ** 2)


def RMSE(actual=None, estimated=None):
    if actual is None or estimated is None:
        raise ValueError("Data cannot be None")
    return np.sqrt(np.mean((actual - estimated) ** 2))


def RelativeRMSE(actual=None, estimated=None):
    if actual is None or estimated is None:
        raise ValueError("Data cannot be None")
    mean = np.mean(actual)
    return (RMSE(actual, estimated) / mean) * 100
