import random
import numpy


def aleatoire(board, last_move):
    not_board = numpy.logical_not(board)
    not_full_cols = []
    for col in range(6):
        if not_board[:, col].any():
            not_full_cols.append(col)
    col = random.choice(not_full_cols)
    not_popped_rows = []
    for row in range(6):
        if board[row, col] == 0:
            not_popped_rows.append(row)
    return col, set(random.choices(not_popped_rows, k=len(not_popped_rows)))
    

algos_all = {"aléatoire": aleatoire}
