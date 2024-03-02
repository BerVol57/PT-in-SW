from src.diag import get_diag
import unittest

def test_get_diag():
    assert get_diag([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 1]]) == [1, 1, 1]

    assert get_diag([[2, 1, 1],
                     [1, 6, 1],
                     [1, 1, 8]]) == [2, 6, 8]

    assert get_diag([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]]) == [1, 1, 1]

    assert get_diag([[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1]]) == [1, 1, 1, 1]

    assert get_diag([[1, 1],
                     [1, 1]]) == [1, 1]

    assert get_diag([[1]]) == [1]


class TestAssertFalse(unittest.TestCase):
    # test function
    def test_assertFalse_get_diag(self):
        self.assertFalse( get_diag([[2, 2], [1, 1]]) == [1], "How?")
