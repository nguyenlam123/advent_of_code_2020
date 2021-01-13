import unittest

from connect_adapter import calc_mul_jolt_diff

class TestJoltDiff(unittest.TestCase):
    def test_ex1(self):
        file = open('day_10/day10Ex.txt', 'r')
        mul_jolt_diff = calc_mul_jolt_diff(file)
        self.assertEqual(mul_jolt_diff, 35)
        file.close()

    def test_ex2(self):
        file = open('day_10/day10Ex2.txt', 'r')
        mul_jolt_diff = calc_mul_jolt_diff(file)
        self.assertEqual(mul_jolt_diff, 220)
        file.close()

    def test_real(self):
        file = open('day_10/day10.txt', 'r')
        mul_jolt_diff = calc_mul_jolt_diff(file)
        self.assertEqual(mul_jolt_diff, 1848)
        file.close()

if __name__ == '__main__':
    unittest.main()