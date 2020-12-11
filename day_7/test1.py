import unittest

from container import get_shiny_gold_containers

class TestContainers(unittest.TestCase):
    def test_1(self):
        file = open('day_7/day7Ex.txt', 'r')
        containers = get_shiny_gold_containers(file)
        self.assertEqual(containers, 4)
        file.close()

    def test_2(self):
        file = open('day_7/day7.txt', 'r')
        containers = get_shiny_gold_containers(file)
        self.assertEqual(containers, 278)
        file.close()

    def test_sibling_zero(self):
        file = open('day_7/day7Ex2.txt', 'r')
        containers = get_shiny_gold_containers(file)
        self.assertEqual(containers, 1)
        file.close()
    
    def test_two_empty_leaf_bags(self):
        file = open('day_7/day7Ex3.txt', 'r')
        containers = get_shiny_gold_containers(file)
        self.assertEqual(containers, 1)
        file.close()
    
    def test_nested_small(self):
        file = open('day_7/day7Ex4.txt', 'r')
        containers = get_shiny_gold_containers(file)
        self.assertEqual(containers, 7)
        file.close()

if __name__ == '__main__':
    unittest.main()