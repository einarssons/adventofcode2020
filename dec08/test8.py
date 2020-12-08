import unittest

import m8

raw_instr = '''\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6\
'''.splitlines()

dec_instr = [
        m8.Instr('nop', 0),
        m8.Instr('acc', 1),
        m8.Instr('jmp', 4),
        m8.Instr('acc', 3),
        m8.Instr('jmp', -3),
        m8.Instr('acc', -99),
        m8.Instr('acc', 1),
        m8.Instr('jmp', -4),
        m8.Instr('acc', 6)
]

class Test8(unittest.TestCase):

    def test_parse_instructions(self):
        for i, raw in enumerate(raw_instr):
            parsed_instr = m8.parse_instruction(raw)
            self.assertEqual(parsed_instr, dec_instr[i], i)

    def test_run_until_loop(self):
        instructions = [m8.parse_instruction(raw) for raw in raw_instr]
        exit = m8.execute_instructions(instructions)
        self.assertEqual(exit.acc, 5)
        self.assertEqual(exit.reason, "loop")

    def test_change_until_success(self):
        instructions = [m8.parse_instruction(raw) for raw in raw_instr]
        acc = m8.change_op_until_success(instructions)
        self.assertEqual(acc, 8)


if __name__ == '__main__':
    unittest.main()
