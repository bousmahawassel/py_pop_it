import random
import os
import json
from game import State


def aleatoire(state):
    moves = state.get_possible_moves()
    move = random.choice(moves)
    return move


def minimax(state):
    return random.choice(state.get_best_moves()[1])


algos_all = {"aleatoire": aleatoire, "minimax": minimax}
