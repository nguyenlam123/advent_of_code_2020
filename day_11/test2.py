import unittest

from seating_sys_ext import get_occupied_seats

class TestSeatsExt(unittest.TestCase):
    def test_ex1(self):
      file = open('day_11/day11Ex1.txt', 'r')
      seats = get_occupied_seats(file)
      self.assertEqual(seats, 26)
      file.close()

    def test_real(self):
      file = open('day_11/day11.txt', 'r')
      seats = get_occupied_seats(file)
      print(seats)
      self.assertEqual(seats, 2131)
      file.close()

if __name__ == '__main__':
    unittest.main()