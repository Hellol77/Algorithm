import sys
from collections import deque
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

a,b=map(int,sys.stdin.readline().split())


def bfs(a,b):
    q=deque()
    q.append(a-1)
    visited=[-1 for i in range(n)]
    visited[a-1]=0
    while q:
        k=q.popleft()
        for i in range(k,n,arr[k]):
            if visited[i]==-1:
                q.append(i)
                visited[i]=visited[k]+1
                if i==b-1:
                    return visited[i]
        for i in range(k,-1,-arr[k]):
            if visited[i]==-1:
                q.append(i)
                visited[i]=visited[k]+1
                if i == b-1:
                    return visited[i]
                    
    return -1
    
print(bfs(a,b))