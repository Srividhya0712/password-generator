# password_gen.py - v1.0
import random
import string
import argparse

def generate_password(length=8, alphanumeric=True):
    if alphanumeric:
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a password.")
    parser.add_argument('--length', type=int, default=8, help='Length of the password')
    parser.add_argument('--alphanumeric', action='store_true', help='Include digits (default: only letters)')

    args = parser.parse_args()
    password = generate_password(args.length, args.alphanumeric)
    print("Generated Password:", password)
