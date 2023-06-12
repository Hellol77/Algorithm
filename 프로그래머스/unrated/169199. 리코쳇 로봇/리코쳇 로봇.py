import collections

def solution(board):
    answer=0
    px,py = 0,0
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    lenX=len(board)
    lenY=len(board[0])
    for i in range(lenX):
        for j in range(lenY):
            if board[i][j]=='R':
                px=i
                py=j
                break
    def bfs():
        d=collections.deque()
        d.append((px,py))
        visited=[[0] *lenY for i in range(lenX)]
        visited[px][py] =1
        
        while d:
            ex,ey=d.popleft()
            if board[ex][ey]=='G':
                return visited[ex][ey]
            for i in range(4):
                kx=ex
                ky=ey
                while True:
                    kx,ky=kx+dx[i],ky+dy[i]
                    if 0<=kx<lenX and 0<=ky<lenY and board[kx][ky]=='D':
                        kx,ky=kx-dx[i],ky-dy[i]
                        break
                    if kx>=lenX or kx<0 or ky>=lenY or ky<0 :
                        kx,ky=kx-dx[i],ky-dy[i]
                        break
            
                if visited[kx][ky]==0:
                    visited[kx][ky]=visited[ex][ey]+1
                    d.append((kx,ky))
                    
        return -1
    
    answer=bfs()
    
    if answer!=-1:
        answer-=1
    return answer
                    