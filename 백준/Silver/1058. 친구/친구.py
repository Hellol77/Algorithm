import sys

n= int(sys.stdin.readline())

arr=[list(sys.stdin.readline().strip()) for i in range(n)]

g=[[0]*n for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if arr[i][j]=='Y' or (arr[i][k]=='Y' and arr[k][j] =='Y'):
                g[i][j]=1

answer=0

for i in g:
    answer=max(answer,sum(i))
print(answer)