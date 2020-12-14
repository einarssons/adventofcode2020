import re


def binstr2int(bstr: str) -> int:
    "Convert string of of type 010101 to int"
    digits = list(bstr)
    nr = 0
    for i in range(len(digits)):
        nr += 1 << i if digits[-(i+1)] == '1' else 0
    return nr


def mask_1_from_str(bstr: str) -> int:
    "Make mask with 1's from bstr"
    symbol = list(bstr)
    mask = 0
    for i in range(len(symbol)):
        mask += 1 << i if symbol[-(i+1)] == '1' else 0
    return mask


def mask_0_from_str(bstr: str) -> int:
    "Make mask with zeros from bstr"
    symbol = list(bstr)
    mask = 0
    for i in range(len(symbol)):
        mask += 1 << i if symbol[-(i+1)] != '0' else 0
    return mask


def mask_x_from_str(bstr: str) -> int:
    "Make mask with 1 for each X in bstr"
    symbol = list(bstr)
    mask = 0
    for i in range(len(symbol)):
        mask += 1 << i if symbol[-(i+1)] == 'X' else 0
    return mask


mask_pattern = re.compile(r'mask = ([01X]+)')
mem_pattern = re.compile(r'mem\[(\d+)\] = (\d+)')


def process_value_v1(value: int, mask0: int, mask1: int) -> int:
    value &= mask0
    value |= mask1
    return value


def execute_program(program: str) -> {}:
    mask0 = 0
    mask1 = 0xffffffffffff
    registers = {}
    lines = program.splitlines()
    for line in lines:
        mobj = mask_pattern.match(line)
        if mobj:
            mask_str = mobj.group(1)
            mask0 = mask_0_from_str(mask_str)
            mask1 = mask_1_from_str(mask_str)
            continue
        mobj = mem_pattern.match(line)
        if mobj:
            val = process_value_v1(int(mobj.group(2)), mask0, mask1)
            registers[int(mobj.group(1))] = val
    return registers


def get_one_positions(n: int) -> [int]:
    "Get positions of 1 bits"
    pos = 0
    ones = []
    while n != 0:
        if n & 0x1 == 1:
            ones.append(pos)
        n = n >> 1
        pos += 1
    return ones


def process_value_v2(addr: int, value: int, mask1: int, mask_x: int) -> {}:
    "Put value in an all addresses made via fuzzy bits."
    new_reg = {}
    addr |= mask1
    addr &= ~mask_x  # Set all mask_x bits to 0
    ones = get_one_positions(mask_x)

    for i in range(1 << len(ones)):
        fuzzy_addr = addr
        for j in range(len(ones)):
            pow_j = 1 << ones[j]
            bit_j = 1 << j
            if i & bit_j != 0:
                fuzzy_addr += pow_j
        new_reg[fuzzy_addr] = value
    return new_reg


def execute_programv2(program: str) -> {}:
    "Execute and sum up all memory values"
    mask_x = 0
    mask1 = 0xffffffffffff
    registers = {}
    lines = program.splitlines()
    for line in lines:
        mobj = mask_pattern.match(line)
        if mobj:
            mask_str = mobj.group(1)
            mask1 = mask_1_from_str(mask_str)
            mask_x = mask_x_from_str(mask_str)
            continue
        mobj = mem_pattern.match(line)
        if mobj:
            addr = int(mobj.group(1))
            val = int(mobj.group(2))
            new_reg = process_value_v2(addr, val, mask1, mask_x)
            registers.update(new_reg)
            continue
        raise ValueError(f"Unknown row: {line}")
    return registers


def main():
    program = open('program.txt').read()
    registers = execute_program(program)
    sum = 0
    for val in registers.values():
        sum += val
    print(f"Total register value is {sum}")
    registers = execute_programv2(program)
    sum = 0
    for val in registers.values():
        sum += val
    print(f"Total register v2 value is {sum}")


if __name__ == "__main__":
    main()
