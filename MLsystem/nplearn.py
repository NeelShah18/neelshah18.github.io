import numpy as np
a = np.array([0,1,2,3,4,5])
print(a)
print(type(a))
print(a.ndim)
print(a.shape)
b = a.reshape((3,2))
print(b)
print(b.ndim)
print(b.shape)
b[1][0]= 77
print(b)
print(a)
c = a.reshape((3,2)).copy()
print(c)
c[0][0] = -99
print(c)
print(a)