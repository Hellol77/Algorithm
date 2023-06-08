import math

def solution(number, limit, power):
    arr=[]
    answer=0
    for i in range(1,number+1):
        g=0
        for j in range(1,math.trunc(math.sqrt(i))+1):
            if i%j == 0:
                g+=2
            if j*j ==i:
                g-=1
                break
        if g>limit:
            answer+=power
        else:
            answer+=g
    
            
    return answer