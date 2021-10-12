import board_util
import test_cases


running = True
while running:
    action_input = input("Press \"t\" to run test cases,\"s\" to input and solve a soduko and \"q\" to quit:")
    if action_input == "t":
        test_cases.run_tests()
    elif action_input == "s":
        rows = []
        row_input = input("Enter row on format on one line:")
        if len(row_input) == 81:
            print(board_util.board_to_string(board_util.get_board(row_input)))
        else:
            print(f"Invalid row length should be 81, is {len(row_input)}")
    elif action_input == "q":
        running = False
    else:
        print("Wrong input, try again")

