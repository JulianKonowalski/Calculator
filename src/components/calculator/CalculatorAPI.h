#ifndef CALCULATOR_API
#define CALCULATOR_API

#include "Calculator.h"

extern "C" { //API FOR PYTHON

Calculator* getCalculator();
void updateNumber(Calculator* c, int input); 
void setOperation(Calculator* c, char operation);
void setFraction(Calculator* c, bool flag);
double calculate(Calculator* c);

}

#endif