import random


class AI:
    def __init__(self, size=6):
        self.size = size
        self.tried = set()
        self.targets = []

    def choose(self, previous_hit=None):
        # After a hit, prefer nearby untried cells.
        if previous_hit is not None:
            r, c = previous_hit

            neighbours = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1)
            ]

            candidates = [
                pos for pos in neighbours
                if 0 <= pos[0] < self.size
                and 0 <= pos[1] < self.size
                and pos not in self.tried
            ]

            self.targets.extend(candidates)

        while self.targets:
            pos = self.targets.pop(0)

            if pos not in self.tried:
                self.tried.add(pos)
                return pos

        options = [
            (r, c)
            for r in range(self.size)
            for c in range(self.size)
            if (r, c) not in self.tried
        ]

        if not options:
            return None

        pos = random.choice(options)
        self.tried.add(pos)

        return pos
