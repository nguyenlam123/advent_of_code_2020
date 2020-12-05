import unittest

from my_seat import find_my_seat

class TestMySeat(unittest.TestCase):
    def test_my_seat(self):
        file = open('day_5/day5.txt', 'r')
        my_seat = find_my_seat(file)
        self.assertEqual(my_seat, 610)
        file.close()

if __name__ == '__main__':
    unittest.main()