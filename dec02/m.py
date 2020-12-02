import re

pattern = re.compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pwd>\w+)")

def check_password(min_len:int, max_len:int, char:str, pwd:str) -> bool:
    "Check if password is valid according to rule defined by min, max, char."
    n=0
    for c in pwd:
        if c == char:
            n += 1
    return min_len <= n <= max_len

def xor(a:bool, b:bool)->bool:
    return (a or b) and not (a and b)

def check_password2(idx1:int, idx2:int, char:str, pwd:str) -> bool:
    "Check if password is valid according to rule defined by idx1, idx2, char."
    return xor(pwd[idx1-1] == char, pwd[idx2-1] == char)

def parse_line(line:str) -> {str:int, str:int, str:str, str:str}:
    "Parse line of form min-max char: pwd and return min, max, char, pwd."
    mobj = pattern.match(line)
    if mobj:
        gd = mobj.groupdict()
        gd['min'] = int(gd['min'])
        gd['max'] = int(gd['max'])
        return gd
    return {"min":0, "max": 0, "char": "", "pwd": ""}

def main(file_name):
    with open(file_name) as ifh:
        n1 = 0
        n2 = 0
        for line in ifh:
            ld = parse_line(line)
            if check_password(ld['min'], ld['max'], ld['char'], ld['pwd']):
                n1 += 1
            if check_password2(ld['min'], ld['max'], ld['char'], ld['pwd']):
                n2 += 1
        print(f"n1={n1}")
        print(f"n2={n2}")

if __name__ == '__main__':
    main('data.txt')

