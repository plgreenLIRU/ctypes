//#include "peteLib.h"
#include <iostream>

int* add(int x[], int y[]){

	static int z[3];

	for (int i=0; i<3; i++){
		z[i] = x[i] + y[i];
	}
	
	return z;
}

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
