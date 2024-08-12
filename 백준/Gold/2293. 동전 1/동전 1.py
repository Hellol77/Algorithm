import sys

n,k = map(int,sys.stdin.readline().split())
arr=[]

dp=[0 for i in range(k+1)]


for i in range(n):
    m = int(sys.stdin.readline())
    if m<=k:
        arr.append(m)

if len(arr)==0:
    print(0)
else:
    for i in range(len(arr)):
        dp[arr[i]]+=1
        for j in range(arr[i],k+1):
            dp[j]+=dp[j-arr[i]]
    print(dp[k])
