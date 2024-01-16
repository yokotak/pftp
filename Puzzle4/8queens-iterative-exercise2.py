#Programming for the Puzzled -- Srini Devadas
#Keep Those Queens Apart
#Given a 8 x 8 chess board, figure out how to place 8 Queens such that
#no Queen attacks another queen.
#This code uses a single-dimensional list to represent Queen positions

#Exercise 1: Add number of solutions to be printed

#This procedure checks that the most recently placed queen on the board on column
#current does not conflict with existing queens.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        #We have two diagonals hence need the abs()
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places 8 Queens on a board so they don't conflict.
#It assumes n = 8 and won't work with other n!
#Additional argument: number of solutions
#Non-default argument needs to be first!
def EightQueens(n=8):
    board = [-1] * n
    location = [-1, 4, -1, -1, -1, -1, -1, 0]

    for i in range(n):
        board[0] = i
        if location[0] != -1:
            board[0] = location[0]
        for j in range(n):
            board[1] = j
            if location[1] != -1:
                board[1] = location[1]
            if not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if location[2] != -1:
                    board[2] = location[2]
                if not noConflicts(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    if location[3] != -1:
                        board[3] = location[3]
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if location[4] != -1:
                            board[4] = location[4]
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if location[5] != -1:
                                board[5] = location[5]
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if location[6] != -1:
                                    board[6] = location[6]
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if location[7] != -1:
                                        board[7] = location[7]
                                    if noConflicts(board, 7):
                                        print (board)
                                    if location[7] != -1:
                                        break
                                if location[6] != -1:
                                    break
                            if location[5] != -1:
                                break
                        if location[4] != -1:
                            break
                    if location[3] != -1:
                        break
                if location[2] != -1:
                    break
            if location[1] != -1:
                break
    return


EightQueens()

