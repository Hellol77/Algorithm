import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
answer=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s=arr[i]+arr[j]+arr[k]
            if s<=m and answer<s:
                answer=s

print(answer)
