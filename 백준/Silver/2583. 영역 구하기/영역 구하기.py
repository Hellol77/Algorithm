import sys
from collections import deque
n,m,k=map(int,sys.stdin.readline().split())

graph=[ [0 for i in range(m)]for i in range(n)]

for i in range(k):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    for j in range(x1,x2):
        for l in range(y1,y2):         
            graph[l][j]=1
            
dx=[0,0,1,-1] 
dy=[1,-1,0,0]
def bfs(x,y):
    global graph
    q=deque()
    q.append((x,y))
    graph[x][y]=1
    answer=1
    while q:
        xx,yy=q.popleft()
        for i in range(4):
            vx=xx+dx[i]
            vy=yy+dy[i]
            if 0<=vx<n and 0<=vy<m and graph[vx][vy]==0:
                graph[vx][vy]=1
                answer+=1
                q.append((vx,vy))
            
    return answer
                
arr=[]


for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            arr.append(bfs(i,j))
            
print(len(arr))
print(*sorted(arr))