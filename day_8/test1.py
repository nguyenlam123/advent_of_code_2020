import unittest

from handheld_halting import get_acc_val

class TestAccVal(unittest.TestCase):
    def test_ex(self):
        file = open('day_8/day8Ex.txt', 'r')
        acc_val = get_acc_val(file)
        self.assertEqual(acc_val, 5)
        file.close()

    def test_real(self):
        file = open('day_8/day8.txt', 'r')
        acc_val = get_acc_val(file)
        self.assertEqual(acc_val, 5)
        file.close()

if __name__ == '__main__':
    unittest.main()