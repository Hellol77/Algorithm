import sys
from collections import deque

n,m,k=map(int,sys.stdin.readline().split())
visited=[[0 for j in range(m+1)]for i in range(n+1)]
arr=[[0 for j in range(m+1)]for i in range(n+1)]

for i in range(k):
    a,b=map(int,sys.stdin.readline().split())
    arr[a][b]=1
dx=[0,0,1,-1]
dy=[1,-1,0,0]
q=deque()
answer=0
def bfs(x,y):
    global answer
    global count
    q.append((x,y))
    while q:
        
        a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0< nx <=m and 0<ny <=n:
                if visited[ny][nx]==0 and arr[ny][nx]==1:
                    q.append((nx,ny))
                    count+=1
                    visited[ny][nx]=1



for i in range(1,n+1):
    for j in range(1,m+1):
        if visited[i][j]==0 and arr[i][j]:
            count=0
            bfs(j,i)
            answer=max(answer, count) 
            
                
print(answer)
                
                
            
    