def four_queens():
    board = [-1] * 4  # initially no queens
    for i in range(4):
        board[0] = i    # place queen in column 0
        for j in range(4):
            board[1] = j  # place queen in column 1
            if not check_board(board): continue
            for k in range(4):
                board[2] = k  # place queen in column 2
                if not check_board(board): continue
                for l in range(4):
                    board[3] = l  # place queen in column 3
                    if check_board(board):
                        return board
    return False
