import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
arr=[]
for i in range(m):
	arr.append(list(map(str,sys.stdin.readline().rstrip())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited=[[0 for i in range(n)]for j in range(m)]
def bfs(x,y,s):
	q=deque()
	count=0
	q.append((x,y))
	visited[y][x]=1
	while q:
		x,y=q.popleft()
		for i in range(4):
			vx=x+dx[i]
			vy=y+dy[i]
			if 0<=vx<n and 0<=vy<m and visited[vy][vx]==0 and arr[vy][vx]==s:
				count+=1
				visited[vy][vx]=1
				q.append((vx,vy))
	return count+1
				
Banswer=0
Wanswer=0

for i in range(m):
	for j in range(n):
		if arr[i][j]=='W' and visited[i][j]==0:
			Wanswer+=bfs(j,i,'W')**2
		elif arr[i][j]=='B' and visited[i][j]==0:
			Banswer+=bfs(j,i,'B')**2


print(Wanswer,Banswer)