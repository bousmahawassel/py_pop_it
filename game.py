import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((6, 6))
        self.last_move = None
        self.previous_board = np.copy(self.board)

    def play(self, col, rows=None):
        self.previous_board = np.copy(self.board)
        try:
            if col not in (0, 1, 2, 3, 4, 5):
                raise ValueError("La colonne doit être comprise entre 0 et 5")
            if rows is None:
                self.board[:, col] = 1
                return
            for row in rows:
                if row not in (0, 1, 2, 3, 4, 5):
                    raise ValueError("La colonne doit être comprise entre 0 et 5")
                if self.board[row][col]:
                    raise ValueError(f"La ligne {row} de la colonne {col} a déjà été jouée !")
                self.board[row][col] = 1
        except Exception:
            self.board = np.copy(self.previous_board)
            raise

    def is_finished(self):
        return self.board.all()
