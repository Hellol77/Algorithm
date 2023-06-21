from collections import deque
def solution(maps):
    answer=[]
    visited = [[0 for i in range(len(maps[0]))] for i in range(len(maps))]
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    x=len(maps)
    y=len(maps[0])
    for i in range(x):
        for j in range(y):
            if maps[i][j]=='X' or visited[i][j]==1:
                continue
            Q=deque()
            Q.append((i,j))
            visited[i][j] = 1
            temp=0
            while Q:
                nx,ny=Q.popleft()
                temp+=int(maps[nx][ny])
                
                for xx,yy in zip(dx,dy):
                    if nx+xx>=x or nx+xx<0 or ny+yy>=y or ny+yy<0 or maps[nx+xx][ny+yy]=='X' or visited[nx+xx][ny+yy]==1:
                        continue
                    else:
                        visited[nx+xx][ny+yy]=1
                        Q.append((nx+xx,ny+yy))
            if temp:
                answer.append(temp)
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
                    
                    
                        
                    
                
                
                
                
                
            
    
    
    