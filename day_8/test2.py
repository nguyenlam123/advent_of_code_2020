import unittest

from corrupt_op import get_acc_val

class TestCorrupt(unittest.TestCase):
    def test_ex(self):
        file = open('day_8/day8Ex.txt', 'r')
        acc_val = get_acc_val(file)
        self.assertEqual(acc_val, 8)
        file.close()

    def test_case(self):
        file = open('day_8/day8.txt', 'r')
        acc_val = get_acc_val(file)
        self.assertEqual(acc_val, 631)
        file.close()

if __name__ == '__main__':
    unittest.main()