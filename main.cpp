#include <iostream>
#include "peteLib.h"

/*
Code illustrating how peteLib.dll can be used from C++. To complie and link to
peteLib.dll:

g++ main.cpp -Link peteLib.dll -o main.exe

*/

int main(){

	const int N = 5;
	float x[N] = {1.1, 2.5, 3.0, 4.2, 5.5};
	float y[N] = {0, 4.2, 1, -2.4, -5.5};
	float z[N];

	add(x, y, z, N);

	for (int i=0; i<N; i++){
		std::cout << z[i] << std::endl;
	}

	return 0;
}
