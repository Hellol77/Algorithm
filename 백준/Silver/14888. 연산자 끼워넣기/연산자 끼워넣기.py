import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

op= list(map(int,sys.stdin.readline().split()))
opList = ["+","-","*","/"]
opArr = []
visited=[]
for i in range(4):
    for j in range(op[i]):
        opArr.append(opList[i])
        visited.append(0)


answer=[]
opAnswer=[]
def p(answer,index):
    global visited,n
    if index==n-1:
        opAnswer.append(answer[:])
        return
    for i in range(n-1):
        if visited[i]==0:
            answer.append(opArr[i])
            visited[i]=1
            p(answer,index+1)
            visited[i]=0
            answer.pop()
        else:
            continue



p(answer,0)

maxAnswer = -1000000000
minAnswer = 1000000000
for i in opAnswer:
    total = arr[0]

    for r in range(1,n):
        if i[r-1] == "+":
            total +=arr[r]
        elif i[r-1] == "-":
            total-=arr[r]
        elif i[r-1] == "*":
            total*=arr[r]
        elif i[r-1]=="/":
            total = int(total/arr[r])
    if total>maxAnswer:
        maxAnswer=total
    if total<minAnswer:
        minAnswer=total

print(maxAnswer)
print(minAnswer)
