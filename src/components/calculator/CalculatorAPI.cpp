#include "CalculatorAPI.h"

Calculator* getCalculator() { return new Calculator(); }
void updateNumber(Calculator* c, int input) { c->updateNumber(input);}
void setOperation(Calculator* c, char operation) { c->setOperation(operation); }
void setFraction(Calculator* c, bool flag) { c->setFraction(flag); }
double calculate(Calculator* c) { return c->calculate(); }