def solution(n):
    arr=[[0]*i for i in range(1,n+1)]
    
    x=0
    y=0
    temp=1
    direction=0
    if n==1:
        return [1]
    while 1:
        arr[x][y]=temp
        temp+=1
        if direction%3==0:
            if 0<=x+1<n and 0<=y<n and arr[x+1][y]==0:
                x+=1
            else:
                direction+=1
                y+=1
                if arr[x][y]!=0:
                    break
        elif direction%3==1 :
            if 0<=x<n and 0<=y+1<n and arr[x][y+1]==0:
                y+=1
            else:
                direction+=1
                x-=1
                y-=1
                if arr[x][y]!=0:
                    break
        elif direction%3==2:
            if 0<=x-1<n and 0<=y-1<n and arr[x-1][y-1]==0:
                x-=1
                y-=1
            else:
                direction+=1
                x+=1
                if arr[x][y]!=0:
                    break
    answer=[]
    
    for i in arr:
        answer.extend(i)
                
            
            
            
            
    return answer