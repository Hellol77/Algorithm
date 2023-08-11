import sys

n=int(sys.stdin.readline())

if n>0:
    dp = [0,1]
    for i in range(2,n+1):
        dp.append((dp[i-2]+dp[i-1])%1000000000)
    print(1)
    print(dp[n])
elif n==0:
    print(0)
    print(0)
else:
    dp=[1,0]
    for i in range(-n):
        temp=dp[i]-dp[i+1]
        if temp<0:
            dp.append(-(abs(temp)%1000000000))
        else:
            dp.append(abs(temp)%1000000000)
    print(-1 if dp[-n+1]<0 else 1)
    print(abs(dp[-n+1]))