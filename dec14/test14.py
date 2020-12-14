import unittest
from dec14 import m14

program = '''
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0\
'''


program2 = '''\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''


class Test14(unittest.TestCase):

    def test_read_number(self):
        nr = '0101'
        self.assertEqual(m14.binstr2int(nr), 0b101, nr)

    def test_read_1mask(self):
        mask = 'X101'
        self.assertEqual(m14.mask_1_from_str(mask), 0b101, mask)

    def test_read_0mask(self):
        mask = 'X101'
        self.assertEqual(m14.mask_0_from_str(mask), 0b1101, mask)

    def test_execute(self):
        registers = m14.execute_program(program)
        self.assertEqual(registers, {8: 64, 7: 101})

    def test_execute_v2(self):
        registers = m14.execute_programv2(program2)
        self.assertEqual(registers,
                         {16: 1, 17: 1, 18: 1, 19: 1, 24: 1, 25: 1,
                          26: 1, 27: 1, 58: 100, 59: 100})


if __name__ == "__main__":
    unittest.main()
