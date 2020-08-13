import numpy as np
from numpy import linalg as alg
# arange
a = np.arange(10, 20, 2)
print('arange =>', a)
# linspace
a = np.linspace(10, 100, 5, endpoint=False, retstep=True)
print('linspace =>', a)

#  copy
print('copy')
a = np.arange(2, 10, 2)
b = np.copy(a)
print(b[:-1:1])

# random array of shape with resize and reshape
a = np.random.rand(10).reshape(2, 5)
print(a)
print('\nresize')
a = np.resize(a, (2, 4))
print(a)

# advance slicing
print('\nslicing')
print(a[:, -1::-1])

# broadcasting
print('\nbroadcasting')
a = np.arange(12).reshape(2, 6)
print('a =>', a)
b = np.arange(20, 24, 2).reshape(2, 1)
print('b =>', b)
print('a+b =>', a + b)

#  attributes
print('shape =>', a.shape)
print('size =>', a.size)
print('dtype =>', a.dtype)
print('ndim =>', a.ndim)

# flatten and ravel
a = np.arange(10, 40, 2).reshape(3, 5)
print('\nwithout flatten or ravel\n', a, '\n')
print(a.flatten(order='f'))
print(a.ravel(order='c'), '\n')

# transpose
a = np.arange(10, 150, 2).reshape(7, 2, 5)
print('transpose\n', a.T)

# split and join
a = np.arange(10, 100).reshape(10, 9)
print('\n', a)
b = np.arange(110, 200).reshape(10, 9)
print('concat :\n', np.concatenate((a, b), axis=1))
print('\n\n')
print(a.shape)
print(a)
print(np.split(a, 3, axis=1), '\n')

#  linear algebras

# inverse of matrix
a = np.arange(1, 5).reshape(2, 2)
print('inverse\n', alg.inv(a) * a, '\n')

# power of matrix
a = np.arange(1, 5).reshape(2, 2)
print(alg.matrix_power(a, 2))

# determinant of matrix
a = np.arange(1, 5).reshape(2, 2)
print('\n', round(alg.det(a)), '\n')
