board = []

def solve(board_to_solve):
    global board
    board = board_to_solve
    _solve()
    return board


def _solve():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for value in range(1, 10):
                    if test_constraints(col, row, value, board):
                        board[row][col] = value
                        if _solve():
                            return True
                        board[row][col] = 0
                return False
    return True

def test_constraints(test_col, test_row, value, board):
    for col in range(9):
        if board[test_row][col] == value:
            return False
    for row in range(9):
        if board[row][test_col] == value:
            return False

    start_row = test_row - test_row % 3
    start_col = test_col - test_col % 3

    for row in range(3):
        for col in range(3):
            if board[start_row + row][start_col + col] == value:
                return False
    return True

