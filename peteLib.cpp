#include <iostream>
#include "peteLib.h"

/*
To compile to shared library
----------------------------

g++ -c -o peteLib.o peteLib.cpp
g++ -shared -o peteLib.dll peteLib.o

*/

void add(int x[], int y[], int z[], int N){
	for (int i=0; i<N; i++){
		z[i] = x[i] + y[i];
	}
}
