from game import Board
from algos_all import algos_all
from algos2 import algos2
from algos1 import algos1

if __name__ == '__main__':
    board = Board()
    is_player_turn = int(input("Voulez-vous commencer en première ou deuxième position ? ")) % 2 != 0
    if is_player_turn:
        algos_all.update(algos2)
    else:
        algos_all.update(algos1)
    algo_name = input(f"Choisissez un algorithme parmi : {', '.join(algos_all.keys())} : ")
    try:
        algo_rank = int(algo_name)
        algo_name = list(algos_all.keys())[algo_rank]
        algo = algos_all[algo_name]
    except ValueError:
        algo = algos_all[algo_name]
    moves = 0
    while not board.is_finished():
        if is_player_turn:
            print(f"C'est au joueur de jouer !")
            col = int(input("Choisissez la colonne entre 0 et 5 : "))
            rows_input = input("Choisissez les rangées, séparées par des virgules (aucun choix siginifie finir "
                               "la colonne) : ").replace(" ", "").split(",")
            if rows_input == [""]:
                rows = None
            else:
                rows = list(map(int, rows_input))
            try:
                board.play(col, rows)
            except Exception as e:
                print(e)
                continue
        else:
            print("C'est à l'algo de jouer !")
            board.play(*algo(board.board, board.last_move))
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
        is_player_turn = not is_player_turn
    if moves % 2 == 0:
        print("Le joueur a gagné !")
    else:
        print("L'algorithme a gagné !")
