from sys import stdin

n=int(stdin.readline())
dp=[float('inf') for i in range(n+1)]
arr=[]
i=1
num=0
while n>num:
    num+=(i*(i+1))//2
    arr.append(num)
    i+=1
for i in range(1,n+1):
    for j in arr:
        if i==j:
            dp[i]=1
            break
        elif j>i:
            break
        dp[i]=min(dp[i],1+dp[i-j])
        
print(dp[n])