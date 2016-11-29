import os
import sys
import importlib
import readchar
from mako.template import Template

class App:
  __instance = None
  def __new__(cls):
    if App.__instance is None:
        App.__instance = object.__new__(cls)
    return App.__instance

  def run(self):
    output = '-'
    canvas = []
    canvas.append([0,0,0,0])
    canvas.append([0,0,0,0])
    canvas.append([0,0,0,0])
    canvas.append([0,0,2,4])

    while True:
      os.system('clear')
      print(Template(filename="controls/views/menu.txt").render())
      print('')
      print(Template(filename="controls/views/canvas.txt").render(canvas=canvas))
      print(Template("=> ${output}").render(output=output))

      command = readchar.readchar()

      if command == '0':
        exit()

      try:
        module_name = Template("controls.controllers.${command}_controller").render(command=command)
        controller_name = Template("${command.upper()}Controller").render(command=command)

        module = importlib.import_module(module_name)
        controller_class = getattr(module, controller_name)

        controller_instance = controller_class()
        output = controller_instance.execute()
      except:
        output = sys.exc_info()[0]
