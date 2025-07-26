import random
import string
import argparse

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure password")
    parser.add_argument("--length", type=int, default=12, help="Length of the password")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols from the password")
    args = parser.parse_args()

    password = generate_password(args.length, not args.no_symbols)
    print("Generated Password:", password)
