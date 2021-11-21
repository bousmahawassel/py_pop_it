
from game import State
from algos2 import improved_symmetric_v2

State.get().build_tree()

insts = State.instances

wins = [inst for inst in insts if inst.get_best_moves()[0]]
wins_states = [inst.state for inst in wins]

not_wins = [inst for inst in insts if not inst.get_best_moves()[0]]
not_wins_states = [inst.state for inst in not_wins]

wins_not_syms = []
for inst in wins:
    try:
        assert improved_symmetric_v2(inst) in inst.get_best_moves()[1]
    except:
        wins_not_syms.append(inst)
wins_not_syms_states = [inst.state for inst in wins_not_syms]
