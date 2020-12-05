import unittest

from boarding_pass import get_seat, max_seat_id

class TestSeatIds(unittest.TestCase):
    def test_1(self):
        file = open('day_5/day5Ex.txt', 'r')
        seats = get_seat(file)
        self.assertEqual(seats, [567, 119, 820])
        max = max_seat_id(seats)
        self.assertEqual(max, 820)
        file.close()
    
    def test_1(self):
        file = open('day_5/day5.txt', 'r')
        seats = get_seat(file)
        max = max_seat_id(seats)
        self.assertEqual(max, 928)
        file.close()

if __name__ == '__main__':
    unittest.main()