#include <iostream>
#include "peteLib.h"

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
