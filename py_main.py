import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer

# Import library
lib_name = "C:\work\ctypes\peteLib.dll"
c_lib = ctypes.CDLL(lib_name)


# Define arrays of size N
N = 4
x = np.array([1, 2, 10, -1])
y = np.array([0, 4, 1, 1])
z = np.zeros([N], dtype=int)

# Define results type
c_lib.add.argtypes = [ndpointer(dtype=ctypes.c_int, shape=(N,)), 
                      ndpointer(dtype=ctypes.c_int, shape=(N,)),
                      ndpointer(dtype=ctypes.c_int, shape=(N,))]


# Add arrays together
c_lib.add(x, y, z, (ctypes.c_int) (N))

# Print result
print(z)
