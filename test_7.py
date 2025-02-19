import numpy as np
import pytest
from task7 import multiplyMatrices

#set up matricies and then assert
def testMultiplyMatrices():
    matrixA = np.array([[1, 2], [3, 4]])
    matrixB = np.array([[5, 6], [7, 8]])
    expected = np.array([[19, 22], [43, 50]])
    result = multiplyMatrices(matrixA, matrixB)
    assert np.array_equal(result, expected), f"Expected {expected} but got {result}"