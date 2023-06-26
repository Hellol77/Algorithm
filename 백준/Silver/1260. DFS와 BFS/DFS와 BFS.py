from collections import deque
import sys
n,m,v = map(int,sys.stdin.readline().split())
graph=[[]for i in range(n+1)]
visited=[0 for i in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()
    
def dfs(v):
    visited[v]=1
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
def bfs(v):
    visited[v]=1
    q=deque()
    q.append(v)
    while q:
        start=q.popleft()
        print(start, end=' ')
        for i in graph[start]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1
                
visited=[0 for i in range(n+1)]
dfs(v)
print()

visited=[0 for i in range(n+1)]
bfs(v)