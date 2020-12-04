import unittest

from get_collisions import get_collisions

class TestCollisions(unittest.TestCase):
    def test_1(self):
        file = open('day3.txt', 'r')
        right = 3
        down = 1
        collsions = get_collisions(file, right, down)
        file.close()
        self.assertEqual(collsions, 234)

    def test_2(self):
        file = open('day3Ex.txt', 'r')
        right = 3
        down = 1
        collsions = get_collisions(file, right, down)
        file.close()
        self.assertEqual(collsions, 7)

    def test_3(self):
        file = open('day3.txt', 'r')
        right = 1
        down = 1
        collsions = get_collisions(file, right, down)
        file.close()
        self.assertEqual(collsions, 79)

    def test_4(self):
        file = open('day3.txt', 'r')
        right = 5
        down = 1
        collsions = get_collisions(file, right, down)
        file.close()
        self.assertEqual(collsions, 72)
    
    def test_5(self):
        file = open('day3.txt', 'r')
        right = 7
        down = 1
        collsions = get_collisions(file, right, down)
        file.close()
        self.assertEqual(collsions, 91)

    def test_6(self):
        file = open('day3.txt', 'r')
        right = 1
        down = 2
        collsions = get_collisions(file, right, down)
        file.close()
        self.assertEqual(collsions, 48)

if __name__ == '__main__':
    unittest.main()