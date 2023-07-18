import sys

r,c,k=map(int,sys.stdin.readline().split())
graph=[]
for i in range(r):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))
answer=0
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def dfs(x,y,count):
    global answer
    if count==k and y==0 and x==c-1:
        answer+=1
    else:
        for i in range(4):
            vx=x+dx[i]
            vy=y+dy[i]
            if 0<= vx < c and 0<=vy <r and graph[vy][vx]!='T':
                graph[vy][vx]='T'
                dfs(vx,vy,count+1)
                graph[vy][vx]='.'
                
graph[r-1][0]='T'
dfs(0, r-1, 1)
print(answer)
                    
    
    
    
