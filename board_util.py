def get_board(board_string):
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(int(board_string[i * 9 + j]))
        board.append(row)
    return board

def board_to_printable_string(board):
    board_string = ""
    for i in range(9):
        if i == 3 or i == 6:
            board_string = board_string + "\n"
        board_string = board_string + "\n"
        for j in range(9):
            if j == 3 or j == 6:
                board_string = board_string + " "
            board_string = board_string + str(board[i][j])
    return board_string

def board_to_string(board):
    board_string = ""
    for row in board:
        for number in row:
            board_string = board_string + str(number)

    return board_string