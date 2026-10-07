class Board:
    SIZE = 6

    def __init__(self):
        self.ships = set()
        self.ship_cells = []
        self.shots = set()
        self.hit_cells = set()

    def place_ship(self, cells):
        cells = set(cells)

        if not cells:
            return

        self.ship_cells.append(cells)
        self.ships.update(cells)

    def fire(self, pos):
        if pos in self.shots:
            return {
                "valid": False,
                "hit": pos in self.ships,
                "sunk": False
            }

        self.shots.add(pos)

        if pos not in self.ships:
            return {
                "valid": True,
                "hit": False,
                "sunk": False
            }

        self.hit_cells.add(pos)

        for ship in self.ship_cells:
            if pos in ship:
                sunk = ship <= self.hit_cells

                return {
                    "valid": True,
                    "hit": True,
                    "sunk": sunk
                }

        return {
            "valid": True,
            "hit": True,
            "sunk": False
        }

    def all_sunk(self):
        return bool(self.ship_cells) and all(
            ship <= self.hit_cells
            for ship in self.ship_cells
        )
