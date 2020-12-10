from dataclasses import dataclass
import re


@dataclass
class Instr():
    op: str
    val: int


@dataclass
class Exit():
    acc: int
    reason: int  # one of loop, outside, success


def parse_instruction(line: str) -> Instr:
    mobj = re.match(r"(?P<op>\w{3}) (?P<val>[-+]\d+)$", line)
    if mobj is None:
        raise ValueError(f"No match for {line}")
    md = mobj.groupdict()
    return Instr(md['op'], int(md['val']))


def execute_instructions(instructions: [Instr]) -> Exit:
    "Execute instructions until loop will start and return accumulator value."
    acc = 0
    nr_steps = 0
    next_instruction = 0
    previous_instructions = []
    while True:
        if next_instruction in previous_instructions:
            return Exit(acc, "loop")
        if next_instruction == len(instructions):
            return Exit(acc, "success")
        if next_instruction > len(instructions):
            return Exit(acc, "outside")
        curr_instruction = next_instruction
        instr = instructions[curr_instruction]
        previous_instructions.append(curr_instruction)
        if instr.op == 'nop':
            next_instruction += 1
        elif instr.op == 'acc':
            acc += instr.val
            next_instruction += 1
        elif instr.op == 'jmp':
            next_instruction += instr.val
        else:
            raise ValueError("Instruction %s not known" % instr.op)
        nr_steps += 1
        # if nr_steps % 100 == 0:
        #    print(f"{nr_steps} steps taken")
        if nr_steps > len(instructions):
            raise Exception("Executing too many instructions")
    return acc


def change_op_until_success(instructions: [Instr]) -> int:
    for idx in range(len(instructions)):
        if instructions[idx].op == "acc":
            continue
        if instructions[idx].op == "nop":
            instructions[idx].op = "jmp"
        else:
            instructions[idx].op = "nop"
        exit = execute_instructions(instructions)
        if exit.reason == "success":
            return exit.acc
        if instructions[idx].op == "nop":
            instructions[idx].op = "jmp"
        else:
            instructions[idx].op = "nop"
    return -100000


def main():
    with open("instructions.txt") as ifh:
        raw_instructions = ifh.read().splitlines()
        instructions = [parse_instruction(raw) for raw in raw_instructions]
        exit = execute_instructions(instructions)
        print(f"Accumulator value before loop is {exit.acc}")
        acc = change_op_until_success(instructions)
        print(f"Accumulator value after success {acc}")


if __name__ == "__main__":
    main()
