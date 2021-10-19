#include "peteLib.h"
#include <iostream>

/*
To compile
----------

g++ -c -o peteLib.o peteLib.cpp
g++ -shared -o peteLib.dll peteLib.o

To link to an execuable written in C++
--------------------------------------

g++ main.cpp -Link peteLib.dll -o main.exe

*/

int* add(int x[], int y[]){

	static int z[3];

	for (int i=0; i<3; i++){
		z[i] = x[i] + y[i];
	}
	
	return z;
}
