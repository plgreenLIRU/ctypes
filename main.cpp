#include "peteLib.h"
#include <iostream>

int main(){

	int x[3] = {1, 2, 3};
	int y[3] = {0, 4, 1};
	int* z;
	
	z = add(x, y);

	for (int i=0; i<3; i++){
		std::cout << z[i] << std::endl;
	}

	return 0;
}
