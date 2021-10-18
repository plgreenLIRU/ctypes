#include "peteLib.h"
#include <iostream>

/*
To compile
----------

g++ -c -o peteLib.o peteLib.cpp
g++ -shared -o peteLib.dll peteLib.o

To link to an execuable written in C++
--------------------------------------

g++ main.cpp -Link peteLib.dll

*/

void add(int x[], int y[]){

	// Summation
	for(int i=0; i<3; i++){
		std::cout << x[i] + y[i] << std::endl;
	}

}
