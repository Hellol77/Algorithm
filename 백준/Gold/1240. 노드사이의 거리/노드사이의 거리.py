import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = [[]for i in range(n+1)]
for i in range(n-1):
	g1,g2,p = map(int,sys.stdin.readline().split())
	graph[g1].append((g2,p))
	graph[g2].append((g1,p))

def bfs(start,end):
	q=deque()
	q.append((start,0))
	visited=[0 for i in range(n+1) ]
	
	while q:
		s,p=q.popleft()
		if s==end:
			return p
		for i,j in graph[s]:
			if visited[i]==0:
				visited[i]=1
				q.append((i,p+j))
		
		
		
		
for i in range(m):
	start,end = map(int,sys.stdin.readline().split())
	print(bfs(start,end))		