import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer
import time

"""
An experiment to see how long each approach takes, specifically comparing:

1. Calling the peteLib library
2. Using a naive Python loop
3. Calling a numpy routine

"""

# Import library
lib_name = "C:\work\ctypes\peteLib.dll"
c_lib = ctypes.CDLL(lib_name)


# Define arrays of, size N, that we want to add together
N = int(1e7)
x = np.random.rand(N).astype(np.float32)
y = np.random.rand(N).astype(np.float32)

# Initalise solution array, where we'll store x+y
z = np.zeros(N, dtype=np.float32)

# Define input types
c_lib.add.argtypes = [ndpointer(dtype=ctypes.c_float, shape=(N,)),
                      ndpointer(dtype=ctypes.c_float, shape=(N,)),
                      ndpointer(dtype=ctypes.c_float, shape=(N,)),
                      ctypes.c_int]

# Add arrays together using C++ compiled code
t1 = time.time()
c_lib.add(x, y, z, N)
dt1 = time.time() - t1

# Add arrays together using a naive for-loop in Python
t2 = time.time()
for i in range(N):
    z[i] = x[i] + y[i]
dt2 = time.time() - t2

# Add arrays together directly using numpy
t3 = time.time()
z = x + y
dt3 = time.time() - t3

# Print results
print("\nNo. points:", N)
print("\nTime taken:\n")
print("Calling peteLib:", dt1, "seconds")
print("Naive Python loop:", dt2, "seconds")
print("numpy:", dt3, "seconds")
