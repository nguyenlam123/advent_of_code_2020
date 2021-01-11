import unittest

from bags_in_shiny_gold import count_bags_in_shiny_gold

class TestBagsInBag(unittest.TestCase):
    def test_one_nested(self):
        file = open('day_7/day7Ex.txt', 'r')
        nbr_bags = count_bags_in_shiny_gold(file)
        self.assertEqual(nbr_bags, 32)
        file.close()

    def test_multiple_nested(self):
        file = open('day_7/day7Ex5.txt', 'r')
        nbr_bags = count_bags_in_shiny_gold(file)
        self.assertEqual(nbr_bags, 126)
        file.close()

    def test_main(self):
        file = open('day_7/day7.txt', 'r')
        nbr_bags = count_bags_in_shiny_gold(file)
        self.assertEqual(nbr_bags, 45157)
        file.close()

    def test_odd(self):
        file = open('day_7/day7Ex6.txt', 'r')
        nbr_bags = count_bags_in_shiny_gold(file)
        self.assertEqual(nbr_bags, 63)
        file.close()

if __name__ == '__main__':
    unittest.main()