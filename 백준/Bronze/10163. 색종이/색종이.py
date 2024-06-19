import sys

n = int(sys.stdin.readline())

arr = [[0 for i in range(1001)] for i in range(1001)]

for i in range(1,n+1):
    row,column,w,h =map(int,sys.stdin.readline().split())
    for r in range(w):
        for c in range(h):
            arr[row+r][column+c]=i

answer = [0]*(n+1)
for i in arr:
    for j in i :
        if j:
            answer[j]+=1
for i in range(1,n+1):
    print(answer[i])
