def check_winner(board):
    """
    Returns:
        "X"  -> X wins
        "O"  -> O wins
        "Tie" -> board is full and no winner
        None -> game is still ongoing
    """
    # All possible winning lines
    lines = (
        board +                                      
        [list(col) for col in zip(*board)] +         
        [[board[i][i] for i in range(3)]] +          
        [[board[i][2-i] for i in range(3)]]          
    )

    # Winner detection
    for line in lines:
        if line[0] in ("X", "O") and line.count(line[0]) == 3:
            return line[0]

    # Check for tie (board full, no spaces)
    if all(cell != " " for row in board for cell in row):
        return "Tie"

    return None
def game_eval(board, turn):
    winner = check_winner(board)

    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if winner == "Tie":
        return 0

    # No winner → evaluate potential immediate win
    lines = (
        board +
        [list(col) for col in zip(*board)] +
        [[board[i][i] for i in range(3)]] +
        [[board[i][2 - i] for i in range(3)]]
    )

    for line in lines:
        if line.count("X") == 2 and line.count(" ") == 1 and turn == "X":
            return 1
        if line.count("O") == 2 and line.count(" ") == 1 and turn == "O":
            return -1

    return 0
board = [
    [" " , " " , "X"],
    [" " , " " , "X"],
    [" " , " " , " "]
]
turn = "O"
print(game_eval(board , turn))