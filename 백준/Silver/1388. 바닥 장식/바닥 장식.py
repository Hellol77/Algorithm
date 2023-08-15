import sys

n,m=map(int,sys.stdin.readline().split())

graph=[]
def dfs(x,y):
    if graph[y][x] =='|':
        graph[y][x]=0
        for i in [1,-1]:
            dy=y+i
            if(0<=dy<n and graph[dy][x])=='|':
                dfs(x,dy)
    elif graph[y][x] =='-':
        graph[y][x]=0
        for i in [1,-1]:
            dx=x+i
            if(0<=dx<m and graph[y][dx])=='-':
                dfs(dx,y)
    
    
    
    
    
    
    
    
    
for i in range(n):
    s=sys.stdin.readline().rstrip()
    graph.append(list(s))
    
answer=0
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0:
            dfs(j,i)
            answer+=1
print(answer)