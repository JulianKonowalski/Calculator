#include "Calculator.h"

void Calculator::updateNumber(const int& input) {
  if(!mOperation && !mNum1Input) { 
    mNum1Input = true;
    delete mNum1;
    mNum1 = nullptr;
  }

  if (mNum1Input) {
    if(mIsFraction) { this->handleFraction(mNum1, input); }
    else { this->handleInt(mNum1, input); }
  }
  else {
    if(mIsFraction) { this->handleFraction(mNum2, input); }
    else { this->handleInt(mNum2, input); }
  }
}

void Calculator::setOperation(const char& operation) {
  if(!mNum1) {
    if(operation == '-') { mNum1 = new double(0); }
    else { return; }
  }

  if(mNum1 && mNum2) { *mNum1 = this->calculate(); }

  if(!mOperation) { mOperation = new char(operation); }
  else { *mOperation = operation; }

  mIsFraction = false;
  mNum1Input = false;
  mFractionPower = 0.1;
}

double Calculator::calculate(void) {
  if(!mNum1) { return 0; }
  else if(!mNum2) { return *mNum1; }

  switch(*mOperation) {
    case '+': 
      *mNum1 += *mNum2;
      break;
    case '-': 
      *mNum1 -= *mNum2;
      break;
    case '*': 
      *mNum1 *= *mNum2;
      break;
    case '/':
      *mNum1 = *mNum2 != 0 ? *mNum1 / *mNum2 : *mNum1;
  }

  delete mOperation;
  mOperation = nullptr;
  delete mNum2;
  mNum2 = nullptr;
  mIsFraction = false;
  mFractionPower = 0.1;

  return *mNum1;
}

void Calculator::handleInt(double*& number, const int& input) {
  if (number == nullptr) { number = new double(input); }
  else { *number = *number * 10 + input; }
}

void Calculator::handleFraction(double*& number, const int& input) {
  if (!number) { number = new double(0); }
  *number += input * mFractionPower;
  mFractionPower *= 0.1;
}