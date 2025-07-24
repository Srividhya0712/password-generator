import unittest
import password_gen

class TestPasswordGenerator(unittest.TestCase):

    def test_password_is_string(self):
        pwd = password_gen.generate_password()
        self.assertIsInstance(pwd, str, "Password should be a string")

    def test_password_not_empty(self):
        pwd = password_gen.generate_password()
        self.assertTrue(len(pwd) > 0, "Password should not be empty")

    def test_password_length_default(self):
        pwd = password_gen.generate_password()
        self.assertEqual(len(pwd), 10, "Password should be 10 characters by default")

    def test_password_is_random(self):
        pwd1 = password_gen.generate_password()
        pwd2 = password_gen.generate_password()
        self.assertNotEqual(pwd1, pwd2, "Passwords should be random")

if __name__ == '__main__':
    unittest.main()
