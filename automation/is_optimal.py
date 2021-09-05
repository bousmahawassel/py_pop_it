import argparse
from algos_all import algos_all
from algos1 import algos1
from algos2 import algos2
from game import State


parser = argparse.ArgumentParser()
parser.add_argument("algo")
parser.add_argument("pos", type=int, choices=[1, 2])
args = parser.parse_args()

if args.pos == 1:
    algo = {**algos_all, **algos1}[args.algo]
else:
    algo = {**algos_all, **algos2}[args.algo]


root = State.get()
root.build_tree()
states = {root}
algo_turn = args.pos == 1
while states:
    next_states = set()
    if algo_turn:
        for state in states:
            algo_move = algo(state)
            assert algo_move in state.get_best_moves()[1], f"L'algo n'est plus gagnant suite au coup {algo_move} " \
                                                           f"dans la position {state.state}"
            next_state = State.get(state.play(algo_move))
            next_states.add(next_state)
    else:
        for state in states:
            next_states.update(state.get_children())
    states = next_states

print("La stratégie est optimale !")
