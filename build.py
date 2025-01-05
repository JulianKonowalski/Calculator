import os
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
  buildDllCommand = ["g++", "-c", "Calculator.cpp", "CalculatorAPI.cpp"]
  compileDllCommand = ["g++", "-static", "-shared", "-o", "Calculator.dll", "Calculator.o", "CalculatorAPI.o"]
  runCommand(buildDllCommand, execPath)
  runCommand(compileDllCommand, execPath)

  print("Generating executable")
  buildExeCommand = ["pyinstaller", "--onefile", "--add-binary", "src/components/calculator/Calculator.dll;.", "--add-data", "src/components/GUI/layout.json;.", "src/main.py"]
  runCommand(buildExeCommand, os.path.dirname(os.path.abspath(__file__)))

  print("Build finished successfuly")