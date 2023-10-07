#!/usr/bin/python3
"""Defines a matrix multi func"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multi of 2 matrix

    Args:
        m_a : The first matrix.
        m_b : The second matrix.
    """

    return (np.matmul(m_a, m_b))