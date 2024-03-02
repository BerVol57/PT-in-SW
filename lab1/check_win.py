import numpy as np


# check win for tic-tac-toe
def check_win(matrix: np.ndarray)->int:
    """
    if element == 1: its 'X' moves
    if element == 0: its 'O' moves
    """
    winner = 'tie'

    if (np.diag(matrix) == 0).all() or (np.diag(np.fliplr(matrix)) == 0).all():
        print("Win player [O]")
        winner = 0
    elif (np.diag(matrix) == 1).all() or (np.diag(np.fliplr(matrix)) == 1).all():
        print("Win player [X]")
        winner = 1
    else:
        for i in range(3):
            if (matrix[i] == 0).all() or (matrix[..., i] == 0).all():
                print("Win player [O]")
                winner = 0
            elif (matrix[i] == 1).all() or (matrix[..., i] == 1).all():
                print("Win player [X]")
                winner = 1

    if winner == 'tie':
        print("Tie")
        return -1
    else:
        return winner

