def solution(targets):
    answer=1
    
    targets.sort(key=lambda x:x[1])
    tempEnd = targets[0][1]
    for i in range(1,len(targets)):
        if tempEnd <= targets[i][0]:
            tempEnd=targets[i][1]
            answer+=1


        
    return answer
            
        
        
        
        
        
    