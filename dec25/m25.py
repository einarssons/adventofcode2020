def loop(subject: int, loop_size: int) -> int:
    value = 1
    for i in range(loop_size):
        value *= subject
        value = value % 20201227
    return value


def find_loopsize(public_key: int) -> int:
    value = 1
    subject = 7
    for i in range(100_000_000):
        value *= subject
        value = value % 20201227
        if value == public_key:
            return i + 1
    raise ValueError("Did not find public key")


def get_secret(public_keys):
    loop_sizes = [find_loopsize(pk) for pk in public_keys]
    enc_key_0 = loop(public_keys[0], loop_sizes[1])
    enc_key_1 = loop(public_keys[1], loop_sizes[0])
    return enc_key_0, enc_key_1


def main():
    public_keys = [11349501, 5107328]
    secret = get_secret(public_keys)
    print(f"The secret is {secret}")


if __name__ == "__main__":
    main()
