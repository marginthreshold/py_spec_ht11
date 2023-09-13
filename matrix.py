import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def __str__(self):
        return f"Matrix:\n {str(self.data)}"

    def __eq__(self, other):
        return np.array_equal(self.data, other.data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Different matrix sizes")
        result_data = self.data + other.data
        return Matrix(result_data)

    def __mul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Different matrix sizes")
        result_data = np.dot(self.data, other.data)
        return Matrix(result_data)


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    print(matrix1)
    print(matrix2)
    print("Matrix comparison:", matrix1 == matrix2)
    sum_matrix = matrix1 + matrix2
    print("Matrix sum is:")
    print(sum_matrix)
    product_matrix = matrix1 * matrix2
    print("Matrix product is:")
    print(product_matrix)
