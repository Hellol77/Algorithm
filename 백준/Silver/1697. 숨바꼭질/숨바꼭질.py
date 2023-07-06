import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())

arr=[0 for i in range(100001)]

def bfs(n):
	q=deque()
	q.append(n)
	while q:
		a=q.popleft()
		if a==k:
			print(arr[a])
			break
		dx=[a+1,a-1,a*2]
		for i in dx:
			if 0<= i <100001 and arr[i]==0:
				arr[i]+=arr[a]+1
				q.append(i)

bfs(n)
			