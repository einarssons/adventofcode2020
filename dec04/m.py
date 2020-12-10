import re


def read_passports(full_text: str) -> []:
    lines = full_text.splitlines()
    pports = []
    pport = ''
    for line in lines:
        if line != '':
            pport += line + ' '
        else:
            pports.append(pport.strip())
            pport = ''
    pports.append(pport.strip())
    return pports


def pport_keys(pport: str) -> []:
    pairs = pport.split()
    keys = []
    for pair in pairs:
        key, value = pair.split(':')
        keys.append(key)
    return keys


def validate_pport_keys(keys: []) -> bool:
    wanted_keys = set(["ecl", "pid", "eyr", "hcl", "byr", "iyr",  "hgt"])
    in_keys = set(keys)
    return in_keys.intersection(wanted_keys) == wanted_keys


def pport_data(pport: str) -> {}:
    pairs = pport.split()
    data = {}
    for pair in pairs:
        key, value = pair.split(':')
        data[key] = value
    return data


def validate_pport(data: dict) -> bool:
    if not validate_pport_keys(data.keys()):
        return False

    if not check_number_interval(data['byr'], 1920, 2002):
        return False
    if not check_number_interval(data['iyr'], 2010, 2020):
        return False
    if not check_number_interval(data['eyr'], 2020, 2030):
        return False
    if not check_height(data['hgt']):
        return False
    if not check_ecl(data['ecl']):
        return False
    if not check_hcl(data['hcl']):
        return False
    if not check_pid(data['pid']):
        return False
    return True


def check_number_interval(val: str, low: int, high: int) -> bool:
    "Check string number vs [low, high] interval"
    # Need conversion and exception handling
    try:
        number = int(val)
    except ValueError:
        return False
    return low <= number <= high


def check_height(height: str) -> bool:
    # Check last two characters
    unit = height[-2:]
    length = height[:-2]
    if unit == 'in':
        return check_number_interval(length, 59, 76)
    elif unit == 'cm':
        return check_number_interval(length, 150, 193)
    else:
        return False


def check_ecl(ecl: str) -> bool:
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in valid_colors


def check_hcl(hcl: str) -> bool:
    return re.match(r'^#[0-9a-f]{6}$', hcl) is not None


def check_pid(pid: str) -> bool:
    return re.match(r'^\d{9}$', pid) is not None


def main():
    with open('passports.txt') as ifh:
        full_text = ifh.read()
        passports = read_passports(full_text)
        valid_keys = 0
        valid_pports = 0
        for pport in passports:
            keys = pport_keys(pport)
            data = pport_data(pport)
            if validate_pport_keys(keys):
                valid_keys += 1
            if validate_pport(data):
                valid_pports += 1
        print('valid keys', valid_keys)
        print(f'valid passports {valid_pports}')


if __name__ == '__main__':
    main()
