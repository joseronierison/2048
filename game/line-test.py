import unittest
from game.line import Line

class LineTest(unittest.TestCase):
  def test_if_move_to_left_with_2_merge(self):
    line = Line([0,0,0,0,2])
    line.merge()

    self.assertEqual(line.fields, [2,0,0,0,0])

  def test_if_move_to_left_and_sum_with_24_merge(self):
    line = Line([0,0,0,2,4])
    line.merge()

    self.assertEqual(line.fields, [2,4,0,0,0])

  def test_if_move_to_left_and_sum_with_22_merge(self):
    line = Line([0,0,0,2,2])
    line.merge()

    self.assertEqual(line.fields, [4,0,0,0,0])

  def test_if_move_to_left_with_and_sum_222_merge(self):
    line = Line([0,0,2,2,2])
    line.merge()

    self.assertEqual(line.fields, [4,2,0,0,0])

  def test_if_move_to_left_and_sum_with_222_merge(self):
    line = Line([0,2,2,2,2])
    line.merge()

    self.assertEqual(line.fields, [4,4,0,0,0])

  def test_if_move_to_left_and_sum_with_only_22_merge(self):
    line = Line([2,2])
    line.merge()

    self.assertEqual(line.fields, [4,0])

  def test_if_move_to_left_and_sum_with_only_222_merge(self):
    line = Line([2,2,2])
    line.merge()

    self.assertEqual(line.fields, [4,2,0])

if __name__ == '__main__':
    unittest.main()