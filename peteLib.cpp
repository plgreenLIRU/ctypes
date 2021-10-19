#include <iostream>
#include "peteLib.h"

/*
Code containing an 'add' method, that can be compiled into a dynamic library.

To compile to a dynamic library:

g++ -c -o peteLib.o peteLib.cpp
g++ -shared -o peteLib.dll peteLib.o

*/

void add(int x[], int y[], int z[], int N){
	/*
	Description
	-----------
		Function for adding two arrays togther

	Parameters
	----------
		x : first array for addition
		y : second array for addtion
		z : array to store x+y
		N : lengh of array

	*/

	for (int i=0; i<N; i++){
		z[i] = x[i] + y[i];
	}
}
