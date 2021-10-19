#include <iostream>
#include "peteLib.h"

/*
To compile
----------

g++ -c -o peteLib.o peteLib.cpp
g++ -shared -o peteLib.dll peteLib.o

To link to an execuable written in C++
--------------------------------------

g++ main.cpp -Link peteLib.dll -o main.exe

*/

void add(int x[], int y[], int z[], int N){

	for (int i=0; i<N; i++){
		z[i] = x[i] + y[i];
	}

}
