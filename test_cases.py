import util
import solver

def run_tests():
    #Fem första testfall från https://www.kaggle.com/bryanpark/sudoku?select=sudoku.csv
    test_boards = [
        "004300209005009001070060043006002087190007400050083000600000105003508690042910300",
        "040100050107003960520008000000000017000906800803050620090060543600080700250097100",
        "600120384008459072000006005000264030070080006940003000310000050089700000502000190",
        "497200000100400005000016098620300040300900000001072600002005870000600004530097061",
        "005910308009403060027500100030000201000820007006007004000080000640150700890000420"
    ]

    solved_boards = [
        "864371259325849761971265843436192587198657432257483916689734125713528694542916378",
        "346179258187523964529648371965832417472916835813754629798261543631485792254397186",
        "695127384138459672724836915851264739273981546946573821317692458489715263562348197",
        "497258316186439725253716498629381547375964182841572639962145873718623954534897261",
        "465912378189473562327568149738645291954821637216397854573284916642159783891736425"
    ]
    print("Original board\t Board solved with solver\t Facit board")

    for test_board, solved_board in zip(test_boards, solved_boards):
        print(util.board_to_string(solver.solve(util.get_board(test_board))) == solved_board)
