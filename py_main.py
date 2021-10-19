import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer

"""
Here we simply create two numpy arrays and add them together using the peteLib
library, which was compiled from C++.
"""

# Import library
lib_name = "C:\work\ctypes\peteLib.dll"
c_lib = ctypes.CDLL(lib_name)


# Define arrays of, size N, that we want to add together
N = 4
x = np.array([0.1, 2, 10.1, -1], dtype=np.float32)
y = np.array([0.6, 4.2, 1, 1], dtype=np.float32)

# Initalise solution array, where we'll store x+y
z = np.zeros(N, dtype=np.float32)

# Define input types
c_lib.add.argtypes = [ndpointer(dtype=ctypes.c_float, shape=(N,)),
                      ndpointer(dtype=ctypes.c_float, shape=(N,)),
                      ndpointer(dtype=ctypes.c_float, shape=(N,)),
                      ctypes.c_int]

# Add arrays together
c_lib.add(x, y, z, N)

# Print result
print(z)
