def solution(board):
    xCount=0
    oCount=0
    oWin=False
    xWin=False
    for i in board:
        oCount+=i.count('O')
        xCount+=i.count('X')
    if oCount < xCount:
        return 0
    if oCount > xCount+1:
        return 0
    if oCount ==0 and xCount == 0 :
        return 1
    flipBoard=list(zip(*board))
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            if board[i][1]=='O':
                oWin=True
            elif board[i][1]=='X':
                xWin=True
                
        if board[0][i]==board[1][i]and board[1][i] ==board[2][i]:
            if board[1][i]=='O':
                oWin=True
            elif board[1][i]=='X':
                xWin=True
    # for i in range(0,3,2):
    #     if board[0][i] == board[1][1] and board[1][1] ==board[2][i-2]:
    #         if board[1][1]=='O':
    #             oWin=True
    #         elif board[1][1]=='X':
    #             xWin=True
    if board[0][0] == board [1][1] and board[1][1]==board[2][2]:
        if board[1][1]=='O':
            oWin=True
        elif board[1][1]=='X':
            xWin=True
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[1][1]=='O':
            oWin=True
        elif board[1][1]=='X':
            xWin=True
    if oWin ==False and xWin==False:
        return 1
    if oWin ==True and xWin ==False:
        if oCount >xCount:
            return 1
    if oWin==False and xWin==True:
        if oCount == xCount:
            return 1
    return 0
        