import os
import shutil
import subprocess

def runCommand(command, directory):
  try:
    subprocess.run(command, cwd=directory, check=True)
  except subprocess.CalledProcessError as error:
    print(f"Command failed with return code {error.returncode}")
    exit(0)
  except Exception as exception:
    print(f"Error: {exception}")
    exit(0)


if __name__ == "__main__":
  execPath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    "src/components/calculator"
  )

  print("Building calculator.dll")
  buildCommand = ["g++", "-c", "Calculator.cpp", "CalculatorAPI.cpp"]
  compileCommand = ["g++", "-static", "-shared", "-o", "Calculator.dll", "Calculator.o", "CalculatorAPI.o"]
  removeCommand = ["rm" "Calculator.o"]
  runCommand(buildCommand, execPath)
  runCommand(compileCommand, execPath)
  print("Build finished successfuly")