import numpy as np
from scipy import linalg

A=np.array([[1,2],[3,4]])
b = np.array([5],[6])
x=np.linalg.solve(A,b)
r=A.dot(x)-b
print(r)