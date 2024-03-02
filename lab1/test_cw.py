from check_win import check_win
import numpy as np


def test_check_win():
    assert check_win(np.array([[1, 1, 0],
                               [1, 0, 1],
                               [1, 0, 1]])) == 1

    assert check_win(np.array([[0, 1, 0],
                               [1, 0, 1],
                               [1, 1, 1]])) == 1

    assert check_win(np.array([[0, 1, 1],
                               [0, 1, 0],
                               [1, 0, 1]])) == 1

    assert check_win(np.array([[1, 1, 0],
                               [1, 1, 1],
                               [1, 0, 1]])) == 1

    assert check_win(np.array([[0, 0, 0],
                               [1, 1, 0],
                               [1, 0, 1]])) == 0

    assert check_win(np.array([[1, 0, 1],
                               [1, 0, 0],
                               [0, 0, 1]])) == 0

    assert check_win(np.array([[0, 1, 0],
                               [1, 0, 1],
                               [1, 0, 0]])) == 0

    assert check_win(np.array([[1, 1, 0],
                               [1, 0, 1],
                               [0, 0, 1]])) == 0

    assert check_win(np.array([[0, 1, 0],
                               [1, 0, 1],
                               [1, 0, 1]])) == -1

    assert check_win(np.array([[0, 1, 0],
                               [0, 1, 1],
                               [1, 0, 1]])) == -1

    assert check_win(np.array([[1, 1, 0],
                               [0, 0, 1],
                               [1, 1, 0]])) == -1

    assert check_win(np.array([[1, 0, 1],
                               [0, 1, 0],
                               [0, 1, 0]])) == -1
