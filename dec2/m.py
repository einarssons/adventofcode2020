
def check_password(min_len:int, max_len:int, char:str, pwd:str) -> bool:
    "Check if password is valid according to rule defined by min, max, char."
    return False


def parse_line(line:str) -> {int, int, str, str}:
    "Parse line of form min-max char: pwd and return min, max, char, pwd."
    return {"min":0, "max": 0, "char": "", "pwd": ""}