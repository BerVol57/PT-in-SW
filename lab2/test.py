import unittest
from eval import *


class TestStringMethods(unittest.TestCase):
    def test_oper(self):
        self.assertEqual(my_eval("32+23"), "55\n")
        self.assertEqual(my_eval("32-23"), "9\n")
        self.assertEqual(my_eval("32*2"), "64\n")
        self.assertEqual(my_eval("(513 - 564)*132"), "-6732\n")
        self.assertEqual(my_eval("(583 + 54)*132"), "84084\n")

    def test_symbol(self):
        self.assertFalse(my_eval("(a+5)"))
        self.assertFalse(my_eval("8/2"))
        self.assertFalse(my_eval("√5"))

    def test_brackets(self):
        self.assertFalse(my_eval(")("))
        self.assertFalse(my_eval("(2+2))"))
        self.assertFalse(my_eval("((2+2)"))
        self.assertFalse(my_eval("(2+(2+2"))
        self.assertFalse(my_eval("2+2)+2)"))


if __name__ == '__main__':
    unittest.main()
