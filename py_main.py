import ctypes
from numpy.ctypeslib import ndpointer

# Import library
lib_name = "C:\work\ctypes\peteLib.dll"
c_lib = ctypes.CDLL(lib_name)

# Define results type
#c_lib.add.restype = ndpointer(dtype=ctypes.c_int, shape=(3,))

# Define arrays of size N
N = 4
x = (ctypes.c_int*N) (1, 2, 10, -1)
y = (ctypes.c_int*N) (0, 4, 1, 1)
z = (ctypes.c_int*N) (0, 0, 0, 0)

# Add arrays together
c_lib.add(x, y, z, (ctypes.c_int) (N))

# Print result
for i in range(N):
    print(z[i])
