import sys

n=int(sys.stdin.readline().rstrip())
dp=[0 for i in range(10000)]
arr=[0 for i in range(10000)]
for i in range(n):
    arr[i]=int(sys.stdin.readline().rstrip())
    
dp[0]=arr[0]
dp[1]=arr[0]+arr[1]
dp[2]=max(arr[0]+arr[2],dp[1],arr[1]+arr[2])
for i in range(3,n):
    dp[i]=max(dp[i-2]+arr[i],arr[i]+arr[i-1]+dp[i-3],dp[i-1])
    
print(max(dp))