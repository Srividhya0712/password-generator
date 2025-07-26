# password_gen.py

import random
import string
import math

def generate_password(length=10, use_letters=True, use_numbers=True, use_symbols=False):
    pool = ''
    if use_letters:
        pool += string.ascii_letters
    if use_numbers:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    if not pool:
        return ''  # Return empty if nothing is selected

    return ''.join(random.choice(pool) for _ in range(length))

def calculate_entropy(length, charset_size):
    # Entropy = length × log2(charset size)
    if charset_size == 0:
        return 0
    return round(length * math.log2(charset_size), 2)
