import sys

n=int(sys.stdin.readline())

l=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())

answer=0
def dfs(num):
    l[num]=-2
    for i in range(len(l)):
        if l[i]==num:
            dfs(i)
            


dfs(m)
for i in range(n):
    if l[i]!=-2 and i not in l:
        answer+=1
print(answer)