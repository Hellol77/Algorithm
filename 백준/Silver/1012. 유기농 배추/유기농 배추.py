import sys
from collections import deque

t=int(sys.stdin.readline())
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[y][x]=1
    while q:
        a,b=q.popleft()
        for i in range(4):
            vx=a+dx[i]
            vy=b+dy[i]
            if 0<=vx<m and 0<=vy<n:
                if visited[vy][vx]==0 and arr[vy][vx]==1:
                    visited[vy][vx]=1
                    q.append((vx,vy))
    return 1
                    
    
                
    
for i in range(t):
    m,n,k=map(int,sys.stdin.readline().split())
    arr=[[0 for i in range(m)]for i in range(n)]
    visited=[[0 for i in range(m)]for i in range(n)]
    answer=0
    for i in range(k):
        x,y=map(int,sys.stdin.readline().split())
        arr[y][x]=1
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0  and arr[i][j]==1:
                answer+=bfs(j,i)
    print(answer)
    


    