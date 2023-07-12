import sys

n,p,q=map(int,sys.stdin.readline().split())

def dfs(N):
    global q,p,arr
    if N==0:
        return 1
    elif N in arr:
        return arr[N]
    arr[N]=dfs(N//p)+dfs(N//q)
    return arr[N]



arr={}
print(dfs(n))