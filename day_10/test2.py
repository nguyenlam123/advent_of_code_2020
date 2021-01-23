import unittest

from distinct_conn import get_nbr_dis_conn

class TestDistinctConn(unittest.TestCase):
    def test_ex1(self):
        file = open('day_10/day10Ex.txt', 'r')
        mul_jolt_diff = get_nbr_dis_conn(file)
        self.assertEqual(mul_jolt_diff, 8)
        file.close()

    def test_ex2(self):
        file = open('day_10/day10Ex2.txt', 'r')
        mul_jolt_diff = get_nbr_dis_conn(file)
        self.assertEqual(mul_jolt_diff, 19208)
        file.close()

    def test_real(self):
        file = open('day_10/day10.txt', 'r')
        mul_jolt_diff = get_nbr_dis_conn(file)
        self.assertEqual(mul_jolt_diff, 8099130339328)
        file.close()

if __name__ == '__main__':
    unittest.main()