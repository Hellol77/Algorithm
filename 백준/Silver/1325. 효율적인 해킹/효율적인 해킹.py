import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())

graph=[[]for i in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[b].append(a)


def bfs(start):
    q=deque()
    q.append(start)
    count=1
    visited=[0 for i in range(n+1)]
    visited[start]=1
    while  q:
        vx=q.popleft()
        for vx in graph[vx]:
            if visited[vx]==0:
                visited[vx]=1
                count+=1
                q.append(vx)
    return count

maxanswer=1
arr=[0 for i in range(n+1)]
for i in range(n+1):
    arr[i]=bfs(i)
for i in range(1,n+1):
    if arr[i]==max(arr):
        print(i,end=' ')