# code of numpy linear algebra 10+5y=2x
import numpy as np
# Represent the system of equations as a matrix equation Ax = b
A = np.array([[-2, 5]])
b = np.array([-10])
# Solve for x (which contains [x, y])
x = np.linalg.lstsq(A, b, rcond=None)[0]
print("Solution:", x)