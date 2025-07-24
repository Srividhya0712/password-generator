# password_gen.py
import random
import string

def generate_password(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("Generated Password:", generate_password())
