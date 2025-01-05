# Calculator

I've made this calculator as a test of combining Python's tkinter frontend with a C++ backend. I'm sure it's full of hidden bugs, but feel free to play with it!

# Compilation

## Requirements
First off make sure you have installed gcc and all of the required packages listed in requirements.txt. If you're using a different compiler, you will have to modify the build.py script. 

## Building the app
There's a build.py script, that will build a dll, link it to the Python frontend and make an .exe file. When you run the .exe file an additional console window will open. You can disable it by adding `--noconsole` flag to the  buildExeCommand in build.py but it will most probably trigger your antivirus, flagging the binary as a trojan. It's normal, due to the way that pyinstaller compiles Python files, so don't worry, I'm not trying to hack you :))