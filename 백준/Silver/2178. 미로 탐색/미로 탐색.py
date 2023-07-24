import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

q=deque()
dx=[0,0,1,-1]
dy=[1,-1,0,0]

graph=[]


for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
def bfs(x,y):
    q.append((x,y))
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0, 0))