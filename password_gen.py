import random
import string
import argparse
import math

WORDS = ["apple", "zebra", "glass", "tree", "cloud", "sun", "light", "mouse", "river", "star"]

def calculate_entropy(length, charset_size):
    return round(length * math.log2(charset_size), 2)

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entropy = calculate_entropy(length, len(characters))
    return password, entropy

def generate_passphrase(num_words=4):
    words = [random.choice(WORDS) for _ in range(num_words)]
    passphrase = '-'.join(words)
    entropy = calculate_entropy(num_words, len(WORDS))
    return passphrase, entropy

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password Generator v1.2")
    parser.add_argument("--length", type=int, default=12, help="Length of password")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--passphrase", action="store_true", help="Generate passphrase instead of password")
    parser.add_argument("--words", type=int, default=4, help="Number of words for passphrase")

    args = parser.parse_args()

    if args.passphrase:
        pwd, entropy = generate_passphrase(args.words)
        print(f"Generated Passphrase: {pwd}")
    else:
        pwd, entropy = generate_password(args.length, not args.no_symbols)
        print(f"Generated Password: {pwd}")
    
    print(f"Entropy: {entropy} bits")
