from game import Board

if __name__ == '__main__':
    board = Board()
    player = 1
    moves = 0
    while not board.is_finished():
        print(f"Le joueur {player} joue !")
        col = int(input("Choisissez la colonne entre 0 et 5 : "))
        rows_input = input("Choisissez les rangées, séparées par des virgules (aucun choix siginifie finir la colonne)"
                           " : ").replace(" ", "").split(",")
        if rows_input == [""]:
            rows = None
        else:
            rows = list(map(int, rows_input))
        try:
            board.play(col, rows)
        except Exception as e:
            print(e)
            continue
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
        if player == 1:
            player = 2
        else:
            player = 1
    if moves % 2 == 0:
        print("Le joueur 1 a gagné !")
    else:
        print("Le joueur 2 a gagné !")
