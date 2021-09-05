import random


def aleatoire(state):
    moves = state.get_possible_moves()
    move = random.choice(moves)
    return move


algos_all = {"aleatoire": aleatoire}
