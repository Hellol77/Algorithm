import sys
from collections import deque
m,n = map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    l=list(map(int,sys.stdin.readline().split()))
    arr.append(l)


dxs = [0,0,1,-1]
dys = [1,-1,0,0]
visited = [ [0 for i in range(m)] for i in range(n)]
answer=0
def dfs(a):
    global answer
    q=deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                answer=a
                q.append((i,j,a+1))
                visited[i][j]=1

    while q:
        (xx,yy,newA) = q.popleft()
        if arr[xx][yy]==1:
            for i in range(4):
                dx=xx+dxs[i]
                dy=yy+dys[i]
                if 0<=dx<n and 0<=dy<m and visited[dx][dy]==0 and arr[dx][dy]==0 and arr[dx][dy]!=-1:
                    answer=newA
                    q.append((dx,dy,newA+1))
                    visited[dx][dy]=1
                    arr[dx][dy]=1
    return

dfs(0)

for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            print(-1)
            exit()

print(answer)
