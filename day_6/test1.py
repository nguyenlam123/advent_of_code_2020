import unittest

from form_answer import get_form_answers

class TestFormAnswers(unittest.TestCase):
    def test_1(self):
        file = open('day_6/day6Ex1.txt', 'r')
        answers = get_form_answers(file)
        self.assertEqual(answers, 6)
        file.close()

    def test_2(self):
        file = open('day_6/day6Ex2.txt', 'r')
        answers = get_form_answers(file)
        self.assertEqual(answers, 11)
        file.close()

    def test_3(self):
        file = open('day_6/day6.txt', 'r')
        answers = get_form_answers(file)
        self.assertEqual(answers, 6565)
        file.close()

if __name__ == '__main__':
    unittest.main()