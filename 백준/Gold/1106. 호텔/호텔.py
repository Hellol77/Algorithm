import sys

c,n=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
	cost,customer=map(int,sys.stdin.readline().split())
	arr.append([cost,customer])
	
dp=[float('inf') for i in range(c+100)]
dp[0]=0

for cost,customer in arr:
	for i in range(customer,c+100):
		dp[i]=min(dp[i-customer]+cost,dp[i])
		
print(min(dp[c:]))
