import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

arr=[]
visited=[[0 for i in range(m)] for i in range(n)]
checked=[]
for i in range(n+1):
    heights=list(map(int,sys.stdin.readline().split()))
    arr.append(heights)

dx=[0,0,-1,1,1,-1,1,-1 ]
dy=[1,-1,0,0,1,-1,-1,1 ]
answer=0
def bfs(x,y):
    global checked
    q=deque()
    q.append((x,y))
    visited[y][x]=1
    check=[(x,y)]
    while q:
        xx,yy=q.popleft()
        for i in range(8):
            vx=xx+dx[i]
            vy=yy+dy[i]
            if 0>vx or 0>vy or n<=vy or m<=vx:
                continue
            if visited[vy][vx]==1:
                continue
            if arr[vy][vx]>arr[y][x]:
                return 0
            if arr[vy][vx]==arr[y][x]:
                check.append((vx,vy))
                q.append((vx,vy))
                visited[vy][vx]=1
        checked+=check
    return 1
    

    
answer=0
for i in range(n):
    for j in range(m):
        if (j,i) not in checked:
            visited=[[0 for i in range(m)] for i in range(n)]
            answer+=bfs(j,i)
 
                
print(answer)
