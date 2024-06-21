import sys

n,m=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    l = list(map(int,sys.stdin.readline().split()))
    arr.append(l)

chicken= []
home = []

for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            chicken.append((i,j))
        elif arr[i][j]==1:
            home.append((i,j))

combinationChicken= []
def c (index,result,r):
    if index==len(chicken):
        if len(result)==r:
            combinationChicken.append(result[:])
        return
    result.append(chicken[index])
    c(index+1,result,r)
    result.pop()
    c(index+1,result,r)


c(0,[],m)
answer=sys.maxsize
for i in combinationChicken:
    tempTotalChikenGap=0
    for (a,b) in home:
        tempChickenGap = sys.maxsize
        for (c,d) in i:
            if tempChickenGap>=abs(a-c)+abs(b-d):
                tempChickenGap=abs(a-c)+abs(b-d)
        tempTotalChikenGap+=tempChickenGap
    if answer>tempTotalChikenGap:
        answer=tempTotalChikenGap

print(answer)
