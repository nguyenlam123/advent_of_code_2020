import unittest

from passports import get_valid_passports

class TestCollisions(unittest.TestCase):
    def test_1(self):
        file = open('day4Ex.txt', 'r')
        valids = get_valid_passports(file)
        file.close()
        self.assertEqual(valids, 2)

    def test_2(self):
        file = open('day4.txt', 'r')
        valids = get_valid_passports(file)
        file.close()
        self.assertEqual(valids, 239)

    def test_3(self):
        file = open('day4Ex2.txt', 'r')
        valids = get_valid_passports(file)
        file.close()
        self.assertEqual(valids, 3)

if __name__ == '__main__':
    unittest.main()