import unittest
import m10

test_jolts1 = '''\
16
10
15
5
1
11
7
19
6
12
4'''

test_jolts2 = '''\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''


class Test10(unittest.TestCase):

    def test_adapter_chain1(self):
        jolts = [int(jolt) for jolt in test_jolts1.splitlines()]
        steps = m10.find_jolt_steps(jolts)
        self.assertEqual(steps.step1 + steps.step2 + steps.step3, len(jolts)+1,
                         "# steps")
        self.assertEqual(steps, m10.Steps(7, 0, 5))

    def test_adapter_chain2(self):
        jolts = [int(jolt) for jolt in test_jolts2.splitlines()]
        steps = m10.find_jolt_steps(jolts)
        self.assertEqual(steps.step1 + steps.step2 + steps.step3, len(jolts)+1,
                         "# steps")
        self.assertEqual(steps, m10.Steps(22, 0, 10))

    def test_sequences1(self):
        jolts = [int(jolt) for jolt in test_jolts1.splitlines()]
        sequences = m10.find_sequences(jolts)
        self.assertEqual(sequences, [3, 2])

    def test_combinations1(self):
        jolts = [int(jolt) for jolt in test_jolts1.splitlines()]
        sequences = m10.find_sequences(jolts)
        combs = m10.find_combinations(sequences)
        self.assertEqual(combs, 8)

    def test_combinations2(self):
        jolts = [int(jolt) for jolt in test_jolts2.splitlines()]
        sequences = m10.find_sequences(jolts)
        print(sequences)
        combs = m10.find_combinations(sequences)
        self.assertEqual(combs, 19208)
