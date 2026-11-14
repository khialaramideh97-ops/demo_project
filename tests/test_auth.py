import unittest
from src.auth import authenticate


class AuthTests(unittest.TestCase):
    def test_valid_credentials_are_accepted(self):
        self.assertTrue(authenticate("student", "pw", "student", "pw"))

    def test_wrong_password_is_rejected(self):
        self.assertFalse(authenticate("student", "wrong", "student", "pw"))

    def test_wrong_username_is_rejected(self):
        self.assertFalse(authenticate("other", "pw", "student", "pw"))

    def test_empty_username_is_rejected(self):
        self.assertFalse(authenticate("", "pw", "student", "pw"))

    def test_empty_password_is_rejected(self):
        self.assertFalse(authenticate("student", "", "student", "pw"))

    def test_none_input_is_rejected_without_crashing(self):
        self.assertFalse(authenticate(None, "pw", "student", "pw"))
        self.assertFalse(authenticate("student", None, "student", "pw"))


if __name__ == "__main__":
    unittest.main()
