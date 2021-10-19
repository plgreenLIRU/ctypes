# ctypes

Some example code written while I was trying to work out how to call complied C++ code from Python. 

## Description
```peteLib.cpp``` contains a method that adds together two arrays of aribtray size. This has been used to create the dynamic library ```peteLib.dll``` (note the 
dll extension as this was written in Windows). 

```main.cpp``` just gives an example of how the ```peteLib``` library can be called from C++.

```py_main.py``` shows how, using ctypes, the ```peteLib.dll``` library can be called from Python, to compute the sum of 2 arrays.

```py_speed_test.py``` is an experiment to check that calling the compiled C++ code is quicker than a naive Python loop.

## The usual warning
This was made as a learning exercise i.e. could be wrong :)

## Updates
- Now processes 32 bit floating point numbers instead of integers.
- Added ```py_speed_test.py``` as an experiment to check speed-up.
