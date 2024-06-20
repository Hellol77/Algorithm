import sys

n,m=map(int,sys.stdin.readline().split())
arr=[i for i in range(1,n+1)]
visied = [0 for i in range(n)]
answer=[]
def p(answer,index):
    global arr,m
    if index==m:
        print(*answer)
        return
    for i in range(n):
        if visied[i]==0:
            answer.append(arr[i])
            visied[i]=1
            p(answer,index+1)
            answer.remove(arr[i])
            visied[i]=0
        else:
            continue


p(answer,0)