import random

class Game:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player = None
        self.robot = None

    # ---------------- Display Board --------------------
    def show_board(self):
        col_width = max(len(str(x)) for row in self.board for x in row)
        top = "┌" + "┬".join("─"*(col_width+2) for _ in self.board[0]) + "┐"
        middle = "├" + "┼".join("─"*(col_width+2) for _ in self.board[0]) + "┤"
        bottom = "└" + "┴".join("─"*(col_width+2) for _ in self.board[0]) + "┘"

        print(top)
        for i, row in enumerate(self.board):
            print("│ " + " │ ".join(str(x).ljust(col_width) for x in row) + " │")
            if i < 2:
                print(middle)
        print(bottom)

    # ---------------- Player Move --------------------
    def choice_maker(self):
        while True:
            try:
                choice = int(input("Enter the block you want to place your move in (1-9): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if not 1 <= choice <= 9:
                print("Choose a number between 1 and 9.")
                continue

            row = (choice - 1) // 3
            col = (choice - 1) % 3

            # Correct empty check
            if self.board[row][col] != " ":
                print("That block is already taken. Try another.")
                continue

            self.board[row][col] = self.player
            return

    # ---------------- Robot Move (simple) --------------------
    def next_move(self):
        """Very basic AI (first available empty cell)."""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.robot
                    return

    # ---------------- Winner Check --------------------
    def check_winner(self):
        lines = (
            self.board +
            [list(col) for col in zip(*self.board)] +             # columns
            [[self.board[i][i] for i in range(3)]] +              # main diagonal
            [[self.board[i][2 - i] for i in range(3)]]            # anti-diagonal
        )

        # Winner detection
        for line in lines:
            if line[0] in ("X", "O") and line.count(line[0]) == 3:
                return line[0]

        # Fixed tie logic
        if all(cell != " " for row in self.board for cell in row):
            return "Tie"

        return None

    # ---------------- Game Evaluator (if needed) --------------------
    def game_eval(self, turn):
        winner = self.check_winner()
        if winner == "X":
            return 1
        if winner == "O":
            return -1
        if winner == "Tie" or winner is None:
            return 0

        lines = (
            self.board +
            [list(col) for col in zip(*self.board)] +
            [[self.board[i][i] for i in range(3)]] +
            [[self.board[i][2-i] for i in range(3)]]
        )

        for line in lines:
            if line.count("X") == 2 and line.count(" ") == 1 and turn == "X":
                return 1
            if line.count("O") == 2 and line.count(" ") == 1 and turn == "O":
                return -1

        return 0

    # ---------------- Main Game Loop --------------------
    def play(self):
        self.player = random.choice(["O", "X"])
        self.robot = "X" if self.player == "O" else "O"

        print(f"You are playing as '{self.player}'")
        if self.player == "O":
            print("Your opponent starts the game...")

        self.show_board()
        status = None

        while status is None:
            # Player move
            self.choice_maker()
            self.show_board()
            status = self.check_winner()
            if status:
                break

            # Robot move
            print("Robot's turn:")
            self.next_move()
            self.show_board()
            status = self.check_winner()

        if status == "Tie":
            print("It's a tie!")
        else:
            print(f"The winner is: {status}")


# ---------------- Run Game --------------------
if __name__ == "__main__":
    Game().play()