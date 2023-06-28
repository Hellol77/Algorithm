import sys

n=int(sys.stdin.readline())
arr=[]
answer=[[0 for i in range(n)]for j in range(n)]
answer[0][0]=1
for i in range(n):
        temp=list(map(int,sys.stdin.readline().split()))
        arr.append(temp)
for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            print(answer[i][j])
            break
        if j+arr[i][j]<=n-1:
            answer[i][j+arr[i][j]]+=answer[i][j]
        if i+arr[i][j]<=n-1:
            answer[i+arr[i][j]][j]+=answer[i][j]
