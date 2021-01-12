import unittest

from encrypt_weak import get_encoding_err

class TestEncodingErr(unittest.TestCase):
    def test_ex(self):
        file = open('day_9/day9Ex.txt', 'r')
        err_val = get_encoding_err(file, 5)
        self.assertEqual(err_val, 62)
        file.close()

    def test_real(self):
        file = open('day_9/day9.txt', 'r')
        err_val = get_encoding_err(file, 25)
        self.assertEqual(err_val, 93727241)
        file.close()

if __name__ == '__main__':
    unittest.main()