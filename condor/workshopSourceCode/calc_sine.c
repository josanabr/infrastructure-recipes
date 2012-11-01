#include <math.h>
#include <stdio.h>
#include "fixed.h"
#define FILETXT SINTXT
#define oper(x) sin(x)

int main() {
	double x = oper(PI4);
	FILE *f = fopen(FILETXT, "w+");
	fprintf(f,"%lf",x*x);
	fclose(f);
}
