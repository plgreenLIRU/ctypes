#include <iostream>
#include "peteLib.h"

/*
Code illustrating how peteLib.dll can be used from C++. To complie and link to
peteLib.dll:

g++ main.cpp -Link peteLib.dll -o main.exe

*/

int main(){

	const int N = 5;
	int x[N] = {1, 2, 3, 4, 5};
	int y[N] = {0, 4, 1, -2, -5};
	int z[N];

	add(x, y, z, N);

	for (int i=0; i<N; i++){
		std::cout << z[i] << std::endl;
	}

	return 0;
}
