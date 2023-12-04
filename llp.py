import numpy as np
from utils import LLP

P = np.array([1, 1, 0, 0, 1])
Q = np.array([0, 0, 0])

K = np.array([[1, 1, 0, 0, 0],
              [0, 0, 0, 1, 0],
              [0, 0, 0, 1, 1]])


P = P.reshape(len(P), 1)
Q = Q.reshape(len(Q), 1)

llp = LLP()

llp.linear_logical_transform(K, P, Q)

for i in range (len(llp.Qh)):
    print(f"\t\tStep #{i + 1}")
    print("P: ")
    print(f"{llp.Ph[i]}")
    print("Q: ")
    print(f"{llp.Qh[i]}")
    print("===================================")


# Q1 = linear_logical_transform(K, P, Q, 1)
# Q2 = linear_logical_transform(K, P, Q, 2)
# print("Q(y) при n = 1:", Q1)
# print("Q(y) при n = 2:", Q2)

# P1 = linear_logical_transform(K.T, Q, P, 1)
# P2 = linear_logical_transform(K.T, Q, P, 2)
# print("P(y) при n = 1:", P1)
# print("P(y) при n = 2:", P2)
