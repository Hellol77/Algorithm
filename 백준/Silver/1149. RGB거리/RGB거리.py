import sys

n=int(sys.stdin.readline())
dp=[[0 for i in range(3)] for i in range(1001)]

arr=[[0 for i in range(3)] for i in range(1001)]

for i in range(1,n+1):
	a,b,c=map(int,sys.stdin.readline().split())
	arr[i][0]=a
	arr[i][1]=b
	arr[i][2]=c
	
for i in range(1,n+1):
	dp[i][0]=min(dp[i-1][1],dp[i-1][2])+arr[i][0]
	dp[i][1]=min(dp[i-1][2],dp[i-1][0])+arr[i][1]
	dp[i][2]=min(dp[i-1][0],dp[i-1][1])+arr[i][2]
	
print(min(dp[n]))

	