import ctypes
from numpy.ctypeslib import ndpointer

# Import library
lib_name = "C:\work\ctypes\peteLib.dll"
c_lib = ctypes.CDLL(lib_name)

# Define results type
c_lib.add.restype = ndpointer(dtype=ctypes.c_int, shape=(3,))

# Add some arrays together
x = (ctypes.c_int*3) (1, 2, 10)
y = (ctypes.c_int*3) (0, 4, 1)
res = c_lib.add(x, y)

# Print results
print(res)
