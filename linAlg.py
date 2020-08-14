import numpy as np
from numpy import linalg as alg
from numpy.ma.core import arange

# eye and identity
a = np.eye(3, k=-2)
print(a)
a = np.identity(3)
print('\n', a, '\n')

# multi and div
a = np.arange(20).reshape(4, 5)
b = np.arange(20, 40).reshape(4, 5)
print('multi\n', np.matmul(a, b.T))  # with a multiply with transpose of b
print("divesion\n", np.divide(a, b, dtype=np.float16), "\n")

# matrix mul shape (3,3) and (3,)
a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 4)
print(np.matmul(a, b))

#  rank of matrix
a = np.arange(1, 10).reshape(3, 3)
print('a :',a)
print('rank of matrix "a" is :',alg.matrix_rank(a))