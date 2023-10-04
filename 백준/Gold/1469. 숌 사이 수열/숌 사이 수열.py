import sys

n=int(sys.stdin.readline())

x=sorted(list(map(int,sys.stdin.readline().split())))
answer=[-1]*2*n
visited=[0]*17
def s(cnt):
    if cnt ==2*n:
        print(*answer)
        exit()
    if answer[cnt]!=-1:
        s(cnt+1)
        return
    for i in x:
        gap=cnt+1+i
        if not visited[i]:
            if gap<2*n and answer[gap]==-1:
                answer[cnt]=i
                answer[gap]=i
                visited[i]=1
                s(cnt+1)
                answer[cnt]=-1
                answer[gap]=-1
                visited[i]=0
                

s(0)
print(-1)


    