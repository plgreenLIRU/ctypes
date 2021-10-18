import ctypes
from numpy.ctypeslib import ndpointer

lib_name = "C:\work\ctypes\peteLib.dll"
c_lib = ctypes.CDLL(lib_name)
##c_lib.add.restype = ndpointer(dtype=ctypes.c_int, shape=(3,))

x = (ctypes.c_int*3) (1, 2, 10)
y = (ctypes.c_int*3) (0, 4, 1)

c_lib.add(x, y)
