#include <math.h>
#include <stdio.h>
#include "fixed.h"
#define FILETXT COSTXT
#define oper(x) cos(x)

int main() {
	double x = oper(PI4);
	FILE *f = fopen(FILETXT, "w+");
	fprintf(f,"%lf",x*x);
	fclose(f);
}
