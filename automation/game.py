class State:
    instances = []

    def __init__(self, state=None, moves=None):
        if not state:
            state = [6, 0, 0, 0, 0, 0, 0]
        self.state = state
        self.moves = moves
        type(self).instances.append(self)
        self.is_finished = self.state == [0, 0, 0, 0, 0, 0, 6]
        self.children = []
        self.value = None
        self.best_moves = None

    def get_possible_moves(self):
        if self.moves is not None:
            return self.moves
        if self.is_finished:
            self.moves = []
            return self.moves
        moves = []
        for i in range(6):
            if self.state[i] > 0:
                for n in range(i + 1, 7):
                    moves.append((i, n))
        self.moves = moves
        return self.moves

    def play(self, move):
        if move not in self.get_possible_moves():
            raise ValueError(f"Le coup {move} n'est pas jouable dans la position {self.state}")
        new_state = [*self.state]
        i, n = move
        new_state[i] -= 1
        new_state[n] += 1
        return new_state

    def get_children(self):
        if self.children:
            return self.children
        if self.is_finished:
            return []
        self.children = [self.get(self.play(move)) for move in self.get_possible_moves()]
        return self.children

    def build_tree(self, depth=None):
        states = {self}
        if not depth:
            while states:
                next_states = set()
                for state in states:
                    if state.children:
                        continue
                    next_states.update(state.get_children())
                states = next_states
        else:
            for i in range(depth):
                if not states:
                    break
                next_states = set()
                for state in states:
                    next_states.update(state.get_children())
                states = next_states

    def get_best_moves(self):
        if self.value is not None and self.best_moves is not None:
            pass
        elif self.is_finished:
            self.value = val = True
            self.best_moves = []
        else:
            best_moves_index = [i for i, val in enumerate(map(lambda child: not child.get_best_moves()[0],
                                                              self.get_children())) if val]
            if best_moves_index:
                self.value = True
                self.best_moves = [self.get_possible_moves()[i] for i in best_moves_index]
            else:
                self.value = False
                self.best_moves = self.get_possible_moves()
        return self.value, self.best_moves

    @classmethod
    def get(cls, state=None):
        if state is None:
            state = [6, 0, 0, 0, 0, 0, 0]
        assert isinstance(state, list)
        assert len(state) == 7
        for instance in cls.instances:
            if instance.state == state:
                return instance
        return cls(state)
