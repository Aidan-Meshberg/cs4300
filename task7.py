import numpy as np

#math part
def multiplyMatrices(matrixA, matrixB):
    return np.dot(matrixA, matrixB)

#setup matricies and send them to mult
matrixA = np.array([[1, 2], [3, 4]])
matrixB = np.array([[5, 6], [7, 8]])
result = multiplyMatrices(matrixA, matrixB)
print("Result:")
print(result)