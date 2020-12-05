import unittest

from passports_validate import get_pass, is_valid, is_valid_byr, is_valid_iyr, is_valid_eyr, is_valid_hgt, is_valid_hcl, is_valid_ecl, is_valid_pid, have_fields

class TestPassports(unittest.TestCase):
    def test_pass_0(self):
        file = open('day_4/day4.txt', 'r')
        valids1 = get_pass(file)
        self.assertEqual(valids1, 188)
        file.close()

    def test_pass_1(self):
        file = open('day_4/day4Invalid.txt', 'r')
        valids2 = get_pass(file)
        self.assertEqual(valids2, 0)
        file.close()
    
    def test_pass_2(self):
        file = open('day_4/day4Valid.txt', 'r')
        valids3 = get_pass(file)
        self.assertEqual(valids3, 4)
        file.close()
    
    def test_pass_3(self):
        file = open('day_4/day4Ex.txt', 'r')
        valids4 = get_pass(file)
        self.assertEqual(valids4, 2)
        file.close()

    def test_pass_4(self):
        file = open('day_4/day4Ex2.txt', 'r')
        valids5 = get_pass(file)
        self.assertEqual(valids5, 3)
        file.close()

    def test_valid_byr(self):
        valid = is_valid_byr('2002')
        self.assertEqual(valid, True)
    
    def test_invalid_byr(self):
        valid = is_valid_byr('2003')
        self.assertEqual(valid, False)
    
    def test_valid_hgt_in(self):
        valid = is_valid_hgt('60in')
        self.assertEqual(valid, True)

    def test_valid_hgt_cm(self):
        valid = is_valid_hgt('190cm')
        self.assertEqual(valid, True)

    def test_invalid_hgt_in(self):
        valid = is_valid_hgt('190in')
        self.assertEqual(valid, False)
    
    def test_invalid_hgt_unit(self):
        valid = is_valid_hgt('190')
        self.assertEqual(valid, False)

    def test_valid_hcl(self):
        valid = is_valid_hcl('#123abc')
        self.assertEqual(valid, True)
    
    def test_invalid_hcl(self):
        valid = is_valid_hcl('#123abz')
        self.assertEqual(valid, False)

    def test_invalid_hcl_three(self):
        valid = is_valid_hcl('#123')
        self.assertEqual(valid, False)

    def test_invalid_hcl_three(self):
        valid = is_valid_hcl('#123')
        self.assertEqual(valid, False)

    def test_invalid_hcl_three_has(self):
        valid = is_valid_hcl('#aaa')
        self.assertEqual(valid, False)

    def test_invalid_hcl_one_char(self):
        valid = is_valid_hcl('z')
        self.assertEqual(valid, False)
    
    def test_valid_ecl(self):
        valid = is_valid_ecl('brn')
        self.assertEqual(valid, True)

    def test_invalid_ecl(self):
        valid = is_valid_ecl('wat')
        self.assertEqual(valid, False)

    def test_validate_pid(self):
        self.assertEqual(is_valid_pid('000000001'), True)
        self.assertEqual(is_valid_pid('0123456789'), False)
        self.assertEqual(is_valid_pid('000000000'), True)
        self.assertEqual(is_valid_pid('11111123456780000'), False)
    
    def test_valid_dict(self):
        my_dict = {
            'byr': '1931',
            'cid': '314',
            'ecl': 'brn',
            'eyr': '2024',
            'hcl': '#ae17e1',
            'hgt': '179cm',
            'iyr': '2013',
            'pid': '820411556'
        }

        valid = is_valid(my_dict)
        self.assertEqual(valid, True)

    def test_valid_dict2(self):
        my_dict = {
            'byr': '1931',
            'ecl': 'brn',
            'eyr': '2024',
            'hcl': '#ae17e1',
            'hgt': '179cm',
            'iyr': '2013',
            'pid': '820411556'
        }

        valid = is_valid(my_dict)
        self.assertEqual(valid, True)
    
    def test_invalid_dict2(self):
        my_dict = {
            'byr': '1931',
            'cid': '314',
            'ecl': 'brn',
            'eyr': '2024',
            'hcl': '#ae17e1',
            'hgt': '179cm',
            'iyr': '2013',
            'pid': '820411556',
            'byr': '1945'
        }

        valid = have_fields(my_dict.keys()) and is_valid(my_dict)
        self.assertEqual(valid, False)

    def test_invalid_dict3(self):
        my_dict = {
            'byr': '1931',
            'cid': '314',
            'ecl': 'brn',
            'eyr': '2024',
            'hcl': '#ae17e1',
            'hgt': '179cm',
            'iyr': '2013'
        }

        valid = is_valid(my_dict)
        self.assertEqual(valid, False)

    def test_invalid_dict4(self):
        my_dict = {
            'byr': '1931',
            'ecl': 'brn',
            'eyr': '2024',
            'hcl': '#ae17e1',
            'hgt': '179cm',
            'iyr': '2013',
            'pid': '820411556',
            'foo': 'bar'
        }

        valid = have_fields(my_dict.keys()) and is_valid(my_dict)
        self.assertEqual(valid, False)


    def test_validate_height(self):
        self.assertEqual(is_valid_hgt('150cm'), True)
        self.assertEqual(is_valid_hgt('149cm'), False)
        self.assertEqual(is_valid_hgt('193cm'), True)
        self.assertEqual(is_valid_hgt('194cm'), False)
        self.assertEqual(is_valid_hgt('75in '), False)
        self.assertEqual(is_valid_hgt('cm150in'), False)
        self.assertEqual(is_valid_hgt('150'), False)
    
    def test_validate_eye_color(self):
        self.assertEqual(is_valid_ecl('blu'), True)
        self.assertEqual(is_valid_ecl('blublu'), False)
        self.assertEqual(is_valid_ecl('aaa'), False)
        self.assertEqual(is_valid_ecl('aaarmbb'), False)
        self.assertEqual(is_valid_ecl('purple'), False)
    
    def test_validate_issue(self):
        self.assertEqual(is_valid_iyr('2010'), True)
        self.assertEqual(is_valid_iyr('2009'), False)
        self.assertEqual(is_valid_iyr('2020'), True)
        self.assertEqual(is_valid_iyr('20200'), False)
        self.assertEqual(is_valid_iyr('2021'), False)
    
    def test_validate_issue(self):
        self.assertEqual(is_valid_byr('1920'), True)
        self.assertEqual(is_valid_byr('1919'), False)
        self.assertEqual(is_valid_byr('2002'), True)
        self.assertEqual(is_valid_byr('2003'), False)
    
    def test_validate_hair_color(self):
        self.assertEqual(is_valid_hcl('#fffaaa'), True)
        self.assertEqual(is_valid_hcl('_#fffaaa_'), False)
        self.assertEqual(is_valid_hcl('#fafafa'), True)
        self.assertEqual(is_valid_hcl('#fafafaf'), False)
        self.assertEqual(is_valid_hcl('#000000'), True)
        self.assertEqual(is_valid_hcl('#123456'), True)
        self.assertEqual(is_valid_hcl('#123abc'), True)
        self.assertEqual(is_valid_hcl('123abc'), False)

    def test_validate_expiration(self):
        self.assertEqual(is_valid_eyr('2020'), True)
        self.assertEqual(is_valid_eyr('2019'), False)
        self.assertEqual(is_valid_eyr('2030'), True)
        self.assertEqual(is_valid_eyr('2031'), False)

if __name__ == '__main__':
    unittest.main()