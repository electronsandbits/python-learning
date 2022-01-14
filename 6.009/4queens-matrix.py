#
# File:4queens-matrix.py
# ---------------------- 
# Given a 4x4 chess board, place 4 Queens so that 
# no two Queens  attach each other by being in the x
# same column,row or diagonal.
# This procedure checks that the most recently  placed queen
# on column current does not conflict with queens in 
# columns to the left

def noConflicts(board, current, qindex, n = 4):

	# Check that there is a single 1 in the current column
	ones = 0
	for i in range (n):
		if board[i][current] == 1:
			ones += 1
			qindex = i
	if on   es >  1:
	    return False
    # Check that the row on the which the current queen is only has on queen on it.

    for j in range(current):
    	if board[index][j] == 1:
    		return False




    # Check the two diagonals from the current Queen	
    # The first loop is for the diagonal /
   
    k = 1
    while qindex - k >= 0 and current - k >= 0:
    	if board[qindex - k][current - k] == 1:
    		return False
    	k += 1
    k = 1
Q2     # The second loop is for the diagonal \		

    while  qindex + K < n  and current - k >= 0:
    	if board[qindex + k][current - k]  == 1:
        k += 1

    return True   		


# This procedure places 4 Queens on a board so they dont conflict
# It assumes n = 4 and won't work with other n!

def FourQueens (n = 4):
	# Initialize the board to be empty
	board = [ [0, 0, 0, 0],
	          [0, 0, 0, 0],
	          [0, 0, 0, 0],
	          [0, 0, 0, 0] ]  

	# Place a queen a column at a time beginning with leftmost column
	for i in range(n):
	    board[i][0]  = 1
	    for j in range(n):
	    	board[j][i] = 1
	    	if noConflicts(board, 1, j, n):
	    		for k in range(n):
	    			board [k][2] = 1
	    			if noConflicts(board, 2, k, n):
	    				for m in range (n):
	    					board[m][3] = 1
	    					if noConflicts(board, 3, m, n):
	    						print (board)
	    					board[m][3]	= 0
	    			board[k][2]	= 0
	    	board[j][1] = 0
	    board[i][0] = 0
	 return   

	FourQueens()


