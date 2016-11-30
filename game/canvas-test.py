import unittest
from game.canvas import Canvas

class CanvasTest(unittest.TestCase):
  def setUp(self):
    self.canvas = Canvas()

  def test_if_create_canvas_matrix_with_length_equal_to_4(self):
    self.assertEqual(len(self.canvas.canvas), 4)

  def test_if_create_canvas_matrix_and_first_line_has_length_equal_to_4(self):
    self.assertEqual(len(self.canvas.canvas[0]), 4)

  def test_if_create_canvas_matrix_and_second_line_has_length_equal_to_4(self):
    self.assertEqual(len(self.canvas.canvas[1]), 4)

  def test_if_create_canvas_matrix_and_third_line_has_length_equal_to_4(self):
    self.assertEqual(len(self.canvas.canvas[2]), 4)

  def test_if_create_canvas_matrix_and_fourth_line_has_length_equal_to_4(self):
    self.assertEqual(len(self.canvas.canvas[3]), 4)

  def test_if_create_canvas_matrix_and_fourth_line_has_length_equal_to_4(self):
    fields = []
    for line in self.canvas.canvas:
      for field in line:
        if field != 0:
          fields.append(field)

    self.assertEqual(len(fields), 2)