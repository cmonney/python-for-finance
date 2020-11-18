import unittest
from UserTesting.user_functions import make_it_uppercase, get_first_word, return_a_list


class TestMyUserFunctions(unittest.TestCase):

    def test_hello_world(self):
        result = make_it_uppercase("hello world")
        self.assertEqual(result, 'HELLO WORLD')

    def test_get_first_word(self):
        result = get_first_word("Lorem ipsum something strange")
        self.assertEqual(result, "Lorem")

    def test_return_a_list(self):
        result = return_a_list()
        self.assertListEqual(result, ["Cat", "Dog", "Bird"])


if __name__ == "__main__":
    unittest.main()
