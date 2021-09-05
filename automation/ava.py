import argparse
from algos_all import algos_all
from algos1 import algos1
from algos2 import algos2
from game import State

parser = argparse.ArgumentParser()
parser.add_argument("algo1")
parser.add_argument("algo2")
parser.add_argument("trial", type=int)
args = parser.parse_args()

algo1 = {**algos_all, **algos1}[args.algo1]
algo2 = {**algos_all, **algos2}[args.algo2]
score = [0, 0]
for _ in range(args.trial):
    state = State.get()
    algo = 1
    moves = 0
    while not state.is_finished:
        if algo == 1:
            move = algo1(state)
            state = State.get(state.play(move))
            algo = 2
        else:
            move = algo2(state)
            state = State.get(state.play(move))
            algo = 1
        moves += 1
    if moves % 2 == 0:
        score[0] += 1
    else:
        score[1] += 1
print(score)
