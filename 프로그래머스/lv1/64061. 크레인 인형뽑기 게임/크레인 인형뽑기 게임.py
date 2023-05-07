def solution(board, moves):
    answer = 0
    stack=[]
    length=len(board)
    for i in moves:
        for j in range(length):
            if board[j][i-1]==0:
                continue
            if stack and board[j][i-1]==stack[-1]:
                stack.pop()
                answer+=2
                board[j][i-1]=0
                break
            stack.append(board[j][i-1])
            board[j][i-1]=0 
            break
    return answer