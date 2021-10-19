import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer

# Import library
lib_name = "C:\work\ctypes\peteLib.dll"
c_lib = ctypes.CDLL(lib_name)


# Define arrays of, size N, that we want to add together
N = 4
x = np.array([1, 2, 10, -1])
y = np.array([0, 4, 1, 1])

# Initalise solution array, where we'll store x+y
z = np.zeros([N], dtype=int)

# Define input types
c_lib.add.argtypes = [ndpointer(dtype=ctypes.c_int, shape=(N,)),
                      ndpointer(dtype=ctypes.c_int, shape=(N,)),
                      ndpointer(dtype=ctypes.c_int, shape=(N,)),
                      ctypes.c_int]

# Add arrays together
c_lib.add(x, y, z, N)

# Print result
print(z)
