class Calculator {
public:
  Calculator() = default;
  ~Calculator() { 
    delete mOperation;
    delete mNum1; 
    delete mNum2; 
  }

  void updateNumber(const int& input);
  void setOperation(const char& operation);
  void setFraction(const bool& flag) { mIsFraction = flag; }
  double calculate(void);

private:

  void handleInt(double*& number, const int& input);
  void handleFraction(double*& number, const int& input);

  char* mOperation = nullptr;
  double* mNum1 = nullptr;
  double* mNum2 = nullptr;
  double mFractionPower = 0.1;
  bool mIsFraction = false;
  bool mNum1Input = true;
};

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

extern "C" { //API FOR PYTHON

Calculator* getCalculator();
void updateNumber(Calculator* c, int input); 
void setOperation(Calculator* c, char operation);
void setFraction(Calculator* c, bool flag);
double calculate(Calculator* c);

}

Calculator* getCalculator() { return new Calculator(); }
void updateNumber(Calculator* c, int input) { c->updateNumber(input);}
void setOperation(Calculator* c, char operation) { c->setOperation(operation); }
void setFraction(Calculator* c, bool flag) { c->setFraction(flag); }
double calculate(Calculator* c) { return c->calculate(); }