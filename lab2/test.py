import unittest
import subprocess
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr

from eval import *


def assert_stdout(self, filepath, expection_stdout, expection_stderr):
    with StringIO() as stdout_buf, StringIO() as stderr_buf:
        with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
            with open(filepath, 'r') as f:
                input_content = f.read()
            result = subprocess.run(["py", "eval.py"], input=input_content, text=True, capture_output=True)
        captured_stdout = result.stdout
        captured_stderr = result.stderr

        self.assertIn(expection_stdout, captured_stdout)
        if expection_stderr == "":
            self.assertEqual(captured_stderr, expection_stderr)
        else:
            self.assertIn(expection_stderr, captured_stderr)


def assert_exit_code(self, filepath, expection_code):
    with open(filepath, 'r') as f:
        input_content = f.read()
    result = subprocess.run(["py", "eval.py"], input=input_content, text=True, capture_output=True)
    self.assertEqual(result.returncode, expection_code)


class TestStringMethods(unittest.TestCase):
    def test_oper(self):
        self.assertEqual(my_eval("32+23"), "55\n")
        self.assertEqual(my_eval("32-23"), "9\n")
        self.assertEqual(my_eval("32*2"), "64\n")
        self.assertEqual(my_eval("(513 - 564)*132"), "-6732\n")
        self.assertEqual(my_eval("(583 + 54)*132"), "84084\n")
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

    def test_stdin_stdout_and_limit(self):
        assert_stdout(self, "test_stdin/test1.txt", "6", "")
        assert_stdout(self, "test_stdin/test_1_number.txt", "456", "")
        assert_stdout(self, "test_stdin/test_1_symbol.txt", "", "Error")
        assert_stdout(self, "test_stdin/test_empty.txt", "", "")
        assert_stdout(self, "test_stdin/test_empty_brackets.txt", "", "Error")
        assert_stdout(self, "test_stdin/test_maxsize_int.txt", str(sys.maxsize + 1), "")
        assert_stdout(self, "test_stdin/test_minsize_int.txt", str(-sys.maxsize - 2), "")

    def test_exit_code(self):
        assert_exit_code(self, "test_stdin/test1.txt", 0)
        assert_exit_code(self, "test_stdin/test_1_symbol.txt", 1)
        assert_exit_code(self, "test_stdin/test_empty_brackets.txt", 1)


if __name__ == '__main__':
    unittest.main()
