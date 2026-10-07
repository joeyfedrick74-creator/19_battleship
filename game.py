from board import Board
from ai import AI


class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI()
        self._setup()

    def _setup(self):
        # All internal coordinates use zero-based (row, col).
        self.player.place_ship({
            (0, 0),
            (0, 1),
            (0, 2)
        })

        self.player.place_ship({
            (3, 3),
            (4, 3)
        })

        self.enemy.place_ship({
            (1, 1),
            (1, 2),
            (1, 3)
        })

        self.enemy.place_ship({
            (4, 4),
            (5, 4)
        })

    def show(self):
        remaining = len(
            self.enemy.ships - self.enemy.hit_cells
        )

        print("\nYour shots are coordinates like 2,3.")
        print("Enemy ship cells remaining:", remaining)
        print("Enter q to quit.")

    def run(self):
        print("Battleship")

        last_ai_hit = None

        while True:
            self.show()

            raw = input("> ").strip().lower()

            if raw == "q":
                print("Game quit.")
                return

            try:
                r, c = map(int, raw.split(","))
                pos = (r - 1, c - 1)

            except (ValueError, TypeError):
                print("Use row,col.")
                continue

            if not (
                0 <= pos[0] < Board.SIZE
                and 0 <= pos[1] < Board.SIZE
            ):
                print("Outside board.")
                continue

            if pos in self.enemy.shots:
                print("Already fired there.")
                continue

            result = self.enemy.fire(pos)

            if result["hit"]:
                print("HIT!")

                if result["sunk"]:
                    print("You sank a ship.")

            else:
                print("MISS!")

            if self.enemy.all_sunk():
                print("You sank the fleet.")
                return

            # AI chooses an internal tuple coordinate.
            ai_pos = self.ai.choose(last_ai_hit)

            if ai_pos is None:
                print("AI has no remaining shots.")
                return

            ai_display = f"{ai_pos[0] + 1},{ai_pos[1] + 1}"

            print("AI fired at", ai_display)

            # Actual AI shot happens here.
            ai_result = self.player.fire(ai_pos)

            if ai_result["hit"]:
                print("AI scored a hit.")

                if ai_result["sunk"]:
                    print("AI sank one of your ships.")
                    last_ai_hit = None
                else:
                    last_ai_hit = ai_pos

            else:
                print("AI missed.")
                last_ai_hit = None

            if self.player.all_sunk():
                print("The AI sank your fleet.")
                return
