import unittest
from password_gen import generate_password, generate_passphrase
import string

class TestPasswordGen(unittest.TestCase):

    def test_password_length(self):
        pwd, _ = generate_password(10)
        self.assertEqual(len(pwd), 10)

    def test_password_no_symbols(self):
        pwd, _ = generate_password(12, False)
        self.assertTrue(all(c not in string.punctuation for c in pwd))

    def test_passphrase_format(self):
        pwd, _ = generate_passphrase(4)
        self.assertEqual(len(pwd.split('-')), 4)

    def test_entropy(self):
        pwd, entropy = generate_password(10)
        self.assertIsInstance(entropy, float)

if __name__ == "__main__":
    unittest.main()
