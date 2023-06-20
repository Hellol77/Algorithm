from collections import deque 
def solution(x, y, n):
    array=[0 for i in range(y+1)]
    Q=deque()
    Q.append(x)
    
    if x==y:
        return 0
    
    while Q:
        nx=Q.popleft()
        
        for i in range(3):
            
            if i==0:
                temp=nx*2
            if i==1:
                temp=nx*3
            if i==2:
                temp=nx+n
            if temp>y or array[temp]:
                continue
            if temp==y:
                return array[nx]+1
            Q.append(temp)
            array[temp]=array[nx]+1
    return -1
            
                