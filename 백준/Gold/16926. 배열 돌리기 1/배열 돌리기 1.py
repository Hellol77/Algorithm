import sys
n,m,r = map(int,sys.stdin.readline().split())

arr=[[0 for i in range(m+1)]]
for i in range(n):
    arr.append([0]+list(map(int,sys.stdin.readline().split())))
for _ in range(r):
    startRow = 1
    endRow = n
    startColumn = 1
    endColumn = m
    while startRow < endRow and startColumn < endColumn:
            # 좌측 위에서 아래로
        temp = arr[endRow][startColumn]
        for i in range(endRow,startRow,-1):
            arr[i][startColumn]=arr[i-1][startColumn]


            # 상단 위 오른쪽에서 위 왼쪽으로
        for i in range(startColumn,endColumn):
            arr[startRow][i]=arr[startRow][i+1]

            # 우측 아래에서 위
        for i in range(startRow,endRow):
            arr[i][endColumn]=arr[i+1][endColumn]

            # 하단 아래 왼쪽에서 위 오른쪽
        for i in range(endColumn,startColumn,-1):
            arr[endRow][i] = arr[endRow][i-1]
        arr[endRow][startColumn+1]=temp
        startRow+=1
        endRow-=1
        startColumn+=1
        endColumn-=1


for i in range(1,n+1):
    print(*arr[i][1:m+1])
