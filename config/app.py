import sys
from app.controller import *

class App:
  __instance = None
  def __new__(cls):
    if App.__instance is None:
        App.__instance = object.__new__(cls)
    return App.__instance

  def run(self):
    print("2048")
    print("Use as setas para comando:")
    while True:
      input_var = input("")