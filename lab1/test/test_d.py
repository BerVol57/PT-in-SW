from src.diag import get_diag


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