import os
import ctypes
from ctypes import cdll

from components.GUI.GUI import GUI

DLL_PATH = os.path.join(
  os.path.dirname(os.path.abspath(__file__)),
  "calculator/Calculator.dll"
)

class App:

  def __init__(self):
    self.gui = GUI(self.__setupBackend())

  def run(self):
    self.gui.run()

  def __setupBackend(self) -> ctypes.CDLL:
    backend = cdll.LoadLibrary(DLL_PATH)

    backend.getCalculator.argtypes = [ctypes.c_void_p]
    backend.getCalculator.restype = ctypes.c_void_p

    backend.updateNumber.argtypes = [ctypes.c_void_p, ctypes.c_int]
    backend.updateNumber.restype = ctypes.c_void_p

    backend.setOperation.argtypes = [ctypes.c_void_p, ctypes.c_char]
    backend.setOperation.restype = ctypes.c_void_p

    backend.setFraction.argtypes = [ctypes.c_void_p, ctypes.c_bool]
    backend.setFraction.restype = ctypes.c_void_p

    backend.calculate.argtypes = [ctypes.c_void_p]
    backend.calculate.restype = ctypes.c_double

    return backend