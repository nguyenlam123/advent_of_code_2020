import unittest

from passports import get_valid_passports

class TestCollisions(unittest.TestCase):
    def test_1(self):
        file = open('day_4/day4Ex.txt', 'r')
        valids = get_valid_passports(file)
        self.assertEqual(valids, 2)
        file.close()

    def test_2(self):
        file = open('day_4/day4.txt', 'r')
        valids = get_valid_passports(file)
        self.assertEqual(valids, 239)
        file.close()

    def test_3(self):
        file = open('day_4/day4Ex2.txt', 'r')
        valids = get_valid_passports(file)
        self.assertEqual(valids, 3)
        file.close()

if __name__ == '__main__':
    unittest.main()