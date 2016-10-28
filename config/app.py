import sys

class App:
  __instance = None
  def __new__(cls):
    if App.__instance is None:
        App.__instance = object.__new__(cls)
    return App.__instance

  def run(self):
    while True:
      input_var = input("Command : ")
      print ("you entered " + input_var)