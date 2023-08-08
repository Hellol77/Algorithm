import sys

n=int(sys.stdin.readline())
arr=[]
dp=[[0,0] for i in range(n)]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    arr.append([a,b])
    
dp[0][0]=arr[0][0]
dp[0][1]=arr[0][1]


for i in range(1,n):
    dp[i][0]=max(dp[i-1][0]+abs(arr[i-1][1]-arr[i][1])+arr[i][0],dp[i-1][1]+abs(arr[i-1][0]-arr[i][1])+arr[i][0])
    dp[i][1]=max(dp[i-1][0]+abs(arr[i-1][1]-arr[i][0])+arr[i][1],dp[i-1][1]+abs(arr[i-1][0]-arr[i][0])+arr[i][1])

print(max(dp[n-1]))