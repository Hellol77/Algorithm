import sys

n,d=map(int,sys.stdin.readline().split())
dp=[i for i in range(d+1)]
temp=[]
for i in range(n):
    start,end,fast = map(int,sys.stdin.readline().split())
    temp.append([start,end,fast])
    
    
for i in range(0,d+1):
    if i>0:
        dp[i]=min(dp[i],dp[i-1]+1)
    for s,e,f in temp:
        if i == s and e<=d and dp[i]+f <dp[e]:
            dp[e]=dp[i]+f
            
print(dp[d])