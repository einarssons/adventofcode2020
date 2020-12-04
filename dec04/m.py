def read_passports(full_text:str)->[]:
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

def pport_keys(pport:str)->[]:
    pairs = pport.split()
    keys = []
    for pair in pairs:
        key, value = pair.split(':')
        keys.append(key)
    return keys

def validate_pport_keys(keys:[])-> bool:
    wanted_keys = set(["ecl", "pid", "eyr", "hcl", "byr", "iyr",  "hgt"])
    in_keys = set(keys)
    return in_keys.intersection(wanted_keys) == wanted_keys

def pport_data(pport:str)->{}:
    pairs = pport.split()
    data = {}
    for pair in pairs:
        key, value = pair.split(':')
        data[key] = value
    return data

def validate_pport(data: dict)-> bool:
    if not validate_pport_keys(data.keys()):
        return False

    if not check_number_interval(data['byr'], 1920, 2002):
        return False
    if not check_number_interval(data['iyr'], 2010, 2020):
        return False
    if not check_number_interval(data['eyr'], 2020, 2030):
        return False
    return True

def check_number_interval(val:str, low:int, high:int)-> bool:
    "Check string number vs [low, high] interval"
    return False


def main():
    with open('passports.txt') as ifh:
        full_text = ifh.read()
        passports = read_passports(full_text)
        valids = 0
        for pport in passports:
            keys = pport_keys(pport)
            if validate_pport_keys(keys):
                valids += 1
        print(valids)

if __name__ == '__main__':
    main()