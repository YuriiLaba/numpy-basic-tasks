import numpy as np

a = np.array([1, 3, 5])
print(a)
print(type(a))

a[2] = a[2]*2
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)

c = np.zeros(shape=(3, 5))
# print(c)

d = np.ones(shape=(4, 6))
# print(d)

c = d
print(c.shape)