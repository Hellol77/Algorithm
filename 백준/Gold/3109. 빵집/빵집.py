import sys

r,c = map(int,sys.stdin.readline().split())
arr=[]
maxRows =[-1]*c
answer=0
for i in range(r):
    l = list(map(str,sys.stdin.readline().rstrip()))
    arr.append(l)

dxs=[-1,0,1]
dys=[1,1,1]
def dfs(x,y,index):
    global answer,maxRows
    if index==c:
        answer+=1
        return True
    for i in range(3):
        dx=dxs[i]+x
        dy=dys[i]+y
        if 0<=dx<r and 0<=dy<c and arr[dx][dy]=='.' and maxRows[dy]<dx:
            arr[dx][dy]='x'
            maxRows[dy]=dx
            if dfs(dx,dy,index+1):
                return True

    return False


for i in range(r):
    dfs(i,0,1)
    arr[i][0]='x'

print(answer)
