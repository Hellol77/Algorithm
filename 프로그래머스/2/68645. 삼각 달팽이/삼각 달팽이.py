def solution(n):
    a=1
    x=-1
    y=0
    arr = [[0] * (i + 1)  for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            if i %3 ==0:
                x+=1
            elif i %3 ==1:
                y+=1
            else:
                x-=1
                y-=1
            arr[x][y]=a
            a+=1

    return sum(arr,[])
            
    
        
        