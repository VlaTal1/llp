import numpy as np
from pprint import pprint as pp


class LLP:
    def __init__(self) -> None:
        self.i = 0
        self.last_Q = None
        self.last_P = None
        self.Ph = []
        self.Qh = []

    def matrix_to_ones(self, matrix: np.array):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > 1:
                    matrix[i][j] = 1

    def linear_logical_transform(self, K: np.ndarray, P: np.ndarray, Q: np.ndarray) -> np.ndarray:
        self.Ph.append(P)
        if self.i % 2 == 0:
            self.i += 1
            new_Q = np.dot(K, P)
            self.matrix_to_ones(new_Q)
            self.last_Q = new_Q

            self.Qh.append(new_Q)
            if np.array_equal(Q, new_Q):
                return new_Q
            else:
                self.linear_logical_transform(K, P, new_Q)

        else:
            self.i += 1
            new_P = np.dot(np.transpose(K), Q)
            self.matrix_to_ones(new_P)
            self.last_P = new_P

            self.Ph.append(new_P)
            if np.array_equal(P, new_P):
                return new_P
            else:
                self.linear_logical_transform(K, new_P, Q)
