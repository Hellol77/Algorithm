import sys

n,k=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    number = int(sys.stdin.readline())
    arr.append(number)
dp=[sys.maxsize for i in range(k+1)]
dp[0]=0
for i in range(n):
    for j in range(arr[i],k+1):
        dp[j]=min(dp[j-arr[i]]+1,dp[j])

if dp[k]==sys.maxsize:
    print(-1)
else:
    print(dp[k])