def symetric(board, last_move):
    col, rows = last_move
    return 6 - col, rows


def intelligent_symetric(board, last_move):
    not_full_cols = []
    for col in range(6):
        if board[:, col].all():
            not_full_cols.append(col)
    if len(not_full_cols) > 2:
        return symetric(board, last_move)
    else:
        if board[:, not_full_cols[0]].sum() == 5:
            return not_full_cols[1],
        elif board[:, not_full_cols[1]].sum() == 5:
            return not_full_cols[0],
        else:
            return symetric(board, last_move)


algos2 = {"symétrique": symetric, "symétrique intelligent": intelligent_symetric}
