import sys

arr=[]
for i in range(9):
    n=int(sys.stdin.readline())
    arr.append(n)
answer=[]

def combi(n, ans,r):
    if n == len(arr):
        if len(ans) == r:
            temp = [i for i in ans]
            answer.append(temp)
        return
    ans.append(arr[n])
    combi(n + 1, ans,r)
    ans.pop()
    combi(n + 1, ans,r)

combi(0,[],7)
for i in answer:
    if sum(i)==100:
        final = i
for i in final:
    print(i)
