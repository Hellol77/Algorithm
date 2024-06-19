import sys

n,m = map(int,sys.stdin.readline().split())

arr = [0]+list(map(int,sys.stdin.readline().split()))
dp = [0]*(n+1)
dp[1]=arr[1]
answer=[]
for i in range(2,n+1):
    dp[i]=dp[i-1]+arr[i]
for num in range(m):
    i,j =map(int,sys.stdin.readline().split())
    if i==j:
        answer.append(arr[i])
        continue
    answer.append(dp[j]-dp[i-1])
for i in answer:
    print(i)
