#ifndef CALCULATOR_H
#define CALCULATOR_H

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

#endif