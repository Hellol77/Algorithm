def solution(scores):
    answer = 0
    ta,tb = scores[0]
    tScore = ta+tb
    
    scores.sort(key=lambda x: (-x[0],x[1]))
    
    maxB = 0
    
    for a,b in scores:
        if ta<a and tb<b:
            return -1
        if b >=maxB:
            maxB=b
            if a+b >tScore:
                answer+=1
                
    return answer+1
    
    
    