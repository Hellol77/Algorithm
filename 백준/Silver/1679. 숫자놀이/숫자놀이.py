import sys

n=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline())

dp=[999999999 for i in range(numbers[-1]*k+2)]

for i in range(1,numbers[-1]*k+2):
	if i in numbers:
		dp[i]=1
	else:
		for j in range(1,i//2+1):
			dp[i]=min(dp[i],dp[j]+dp[i-j])
	if dp[i]>k:
		if i%2==0:
			t='holsoon'
		else:
			t='jjaksoon'
		print(f"{t} win at {i}")
		break
	
