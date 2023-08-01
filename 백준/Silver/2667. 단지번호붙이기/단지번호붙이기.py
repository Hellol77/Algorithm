import sys
from collections import deque

n=int(sys.stdin.readline())

graph=[]
ans=[]
for i in range(n):
    m=sys.stdin.readline().rstrip()
    graph.append(list(m))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    global graph
    q=deque()
    q.append((x,y))
    answer=1
    graph[x][y]='0'
    while q:
        xx,yy=q.popleft()
        for i in range(4):
            vx=xx+dx[i]
            vy=yy+dy[i]
            if 0<=vx<n and 0<=vy<n and graph[vx][vy]=='1':
                graph[vx][vy]='0'
                answer+=1
                q.append((vx,vy))
                
    return answer
for i in range(n):
    for j in range(n):
        if graph[i][j]=='1':
            ans.append(bfs(i,j))
            
print(len(ans))
for i in sorted(ans):
    print(i)