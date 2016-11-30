from random import randint

class Canvas:
  def __init__(self):
    self.canvas = self.build_canvas()


  def build_canvas(self):
    canvas = []
    count = 0
    for x in range(0, 4):
      line = []
      for y in range(0, 4):
        field_value = randint(2,4)
        if ((field_value == 2 or field_value == 4) and count < 2):
          count += 1
        else:
          field_value=0
        line.append(field_value)
      canvas.append(line)

    return canvas
