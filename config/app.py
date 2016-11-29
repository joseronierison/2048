import readchar
import os
#from app.controller import *

class App:
  __instance = None
  def __new__(cls):
    if App.__instance is None:
        App.__instance = object.__new__(cls)
    return App.__instance

  def run(self):
    input_var = ''
    while True:
      os.system('clear')
      print("2048 by José Roniérison")
      print("Use: ")
      print(" - w to up:")
      print(" - s to down:")
      print(" - a to left:")
      print(" - d to left:")
      print("----------------")
      print(" - q to quit:")
      print(input_var)

      if(input_var == 'q'):
        exit()

      input_var = readchar.readchar()
      print(input_var)