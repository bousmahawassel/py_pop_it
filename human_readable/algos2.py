import numpy as np


def symmetric(board, last_move):
    col, rows = last_move
    return 5 - col, rows


def improved_symmetric(board, last_move):
    not_full_cols = []
    for col in range(6):
        if not board[:, col].all():
            not_full_cols.append(col)
    if len(not_full_cols) > 2:
        return symetric(board, last_move)
    elif len(not_full_cols) == 1:
        print(not_full_cols)
        col = board[:, not_full_cols[0]]
        print(col)
        zeros = np.where(col == 0)[0]
        print(zeros)
        zeros = np.delete(zeros, 0)
        print(zeros)
        return not_full_cols[0], list(zeros)
    else:
        if board[:, not_full_cols[0]].sum() == 5:
            return not_full_cols[1],
        elif board[:, not_full_cols[1]].sum() == 5:
            return not_full_cols[0],
        else:
            return symetric(board, last_move)


def improved_symmetric_v2(board, last_move):
    full_cols = []
    almost_full_cols = []
    for col in range(6):
        if np.count_nonzero(board[:, col]) == 6:
            full_cols.append(col)
        elif np.count_nonzero(board[:, col]) == 5:
            almost_full_cols.append(col)
    if len(full_cols) + len(almost_full_cols) > 4:
        return symmetric(board, last_move)


algos2 = {"sym": symmetric, "symp": intelligent_symmetric, "symp_v2": improved_symmetric_v2}
