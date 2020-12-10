import unittest
from collections import namedtuple

import m


TestCase = namedtuple('TestCase', ['name', 'full_text', 'want'])


example_passports = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in\
"""

adv_examples = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719\
"""


pport = ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd " +
         "byr:1937 iyr:2017 cid:147 hgt:183cm")


class TestDec4(unittest.TestCase):

    def test_read_passports(self):
        passports = m.read_passports(example_passports)
        self.assertEqual(len(passports), 4, "Right number of passports")

    def test_passport_keys(self):
        keys = m.pport_keys(pport)
        self.assertEqual(keys, ["ecl", "pid", "eyr", "hcl", "byr",
                         "iyr", "cid", "hgt"], "Keys")

    def test_key_validation(self):
        self.assertEqual(m.validate_pport_keys(["ecl", "pid", "eyr", "hcl",
                                                "byr", "iyr", "cid", "hgt"]),
                         True, "8 keys")
        self.assertEqual(m.validate_pport_keys(["ecl", "pid", "eyr", "hcl",
                                                "byr", "iyr",  "hgt"]),
                         True, "7 keys no cid")
        self.assertEqual(m.validate_pport_keys(["ecl", "pid", "eyr", "hcl",
                                                "byr", "iyr", "cid"]),
                         False, "7 keys with cid")

    def test_full_validation(self):
        pports = m.read_passports(adv_examples)
        expected_results = (False, False, False, False, True, True, True, True)
        for result, pport in zip(expected_results, pports):
            data = m.pport_data(pport)
            self.assertEqual(m.validate_pport(data), result, data)

    def test_check_number_interval(self):
        self.assertEqual(m.check_number_interval("1922", 1920, 2002),
                         True, "Valid number")
        self.assertEqual(m.check_number_interval("1919", 1920, 2002),
                         False, "Non-Valid number")
        self.assertEqual(m.check_number_interval("arne", 1920, 2002),
                         False, "Non-number")

    def test_check_height(self):
        self.assertEqual(m.check_height("60in"), True, "Valid 60in")
        self.assertEqual(m.check_height("190cm"), True, "Valid 190cm")
        self.assertEqual(m.check_height("190in"), False, "Bad 190in")
        self.assertEqual(m.check_height("190"), False, "Bad 190")

    def test_check_ecl(self):
        self.assertEqual(m.check_ecl("brn"), True, "Good brn")
        self.assertEqual(m.check_ecl("wat"), False, "Bad wat")

    def test_check_hcl(self):
        self.assertEqual(m.check_hcl("#123abc"), True, "Good 1")
        self.assertEqual(m.check_hcl("#123abz"), False, "Bad z")
        self.assertEqual(m.check_hcl("123abz"), False, "Bad no #")

    def test_check_pid(self):
        self.assertEqual(m.check_pid("000000001"), True, "9 digits")
        self.assertEqual(m.check_pid("0123456789"), False, "10 digits")
        self.assertEqual(m.check_pid("012a456789"), False, "Non-digits")


if __name__ == '__main__':
    unittest.main()
