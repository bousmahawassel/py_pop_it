from game import Board
from algos_all import algos_all
from algos2 import algos2
from algos1 import algos1

if __name__ == '__main__':
    board = Board()
    algos_start = {**algos_all, **algos1}
    algos_not_start = {**algos_all, **algos2}
    is_first_turn = True
    algo_start_name = input(f"Choisissez un algorithme parmi : {', '.join(algos_start.keys())} : ")
    try:
        algo_start_rank = int(algo_start_name)
        algo_start_name = list(algos_start.keys())[algo_start_rank]
        algo_start = algos_start[algo_start_name]
    except ValueError:
        algo = algos_start[algo_start_name]
    algo_not_start_name = input(f"Choisissez un algorithme parmi : {', '.join(algos_not_start.keys())} : ")
    try:
        algo_not_start_rank = int(algo_name)
        algo_not_start_name = list(algos_not_start.keys())[algo_not_start_rank]
        algo_not_start = algos_not_start[algo_not_start_name]
    except ValueError:
        algo_not_start = algos_not_start[algo_not_start_name]
    moves = 0
    while not board.is_finished():
        if is_first_turn:
            print(f"C'est au premier algorithme de jouer !")
            board.play(*algo_start(board.board, board.last_move)
        else:
            print("C'est à l'algo de jouer !")
            board.play(*algo_not_start(board.board, board.last_move))
        board_as_str = ""
        for row in board.board:
            for item in row:
                if item:
                    board_as_str += "◯"
                else:
                    board_as_str += "⬤"
                board_as_str += "\t"
            board_as_str += "\n"
        print(board_as_str)
        moves += 1
        is_first_turn = not is_first_turn
    if moves % 2 == 0:
        print("Le premier algorithme a gagné !")
    else:
        print("Le deuxième algorithme a gagné !")
