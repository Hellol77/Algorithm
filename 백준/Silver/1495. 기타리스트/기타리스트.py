import sys

n,s,m = map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
dp=[[0 for i in range(m+1)]for i in range(n+1)]
dp[0][s]=1

for i in range(n):
	for j in range(m+1):
		if dp[i][j]==1:
			if j+arr[i]<=m:
				dp[i+1][j+arr[i]]=1
			if 0<=j-arr[i]:
				dp[i+1][j-arr[i]]=1

answer = -1

for i in range(m,-1,-1):
	if dp[n][i]==1:
		answer=i
		break
print(answer)