#Programming for the Puzzled -- Srini Devadas
#Keep Those Queens Apart
#Given a 8 x 8 chess board, figure out how to place 8 Queens such that
#no Queen attacks another queen.
#This code uses a single-dimensional list to represent Queen positions


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
def EightQueens(n=8):
    board = [-1] * n
    #boardに代入していくためのボックスを作成
    piece = [0] * n
    #ループの開始
    while piece[0] < 8:
        #衝突のフラグ
        flag = 'False'
        board[0] = piece[0]
        for i in range(1, n):
            board[i] = piece[i]
            if not noConflicts(board, i):
                flag = 'True'
                break
        if flag == 'True':
            for k in range(i, -1, -1):
                if piece[k] < 7:
                    piece[k] += 1
                    break
                if k == 0 and piece[k] == 7:
                    piece[k] += 1
            if k != n-1 and piece[k] != 8:
                for l in range(k+1, n):
                    piece[l] = 0
            continue
        print(board)
        for k in range(n-1, -1, -1):
            if piece[k] < 7:
                piece[k] += 1
                break
        if k != n-1:
            for l in range(k+1, n):
                piece[l] = 0
        continue
        
    return


EightQueens()
