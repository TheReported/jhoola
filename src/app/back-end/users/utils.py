import random
import string


def generate_password():
    chars = [char for char in string.printable if char not in string.whitespace]
    return ''.join(random.choice(chars) for _ in range(12))
