def solution(picks, minerals):
    sum=0
    answer=0
    for i in picks:
        sum+=i
    
    if sum*5<len(minerals):
        minerals=minerals[:sum*5]
        
    arr=[[0,0,0] for i in range(10)]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            arr[i//5][0]+=1
        elif minerals[i]=='iron':
            arr[i//5][1]+=1
        elif minerals[i]=='stone':
            arr[i//5][2]+=1

            
    arr=sorted(arr,key=lambda x: (-x[0],-x[1],-x[2]))
            
        
        
    

        
    for dia,iron,stone in arr:
        for i in range(len(picks)):
            if picks[0]>0:
                picks[0]-=1
                answer+=dia+iron+stone
                break
            elif picks[1]>0:
                picks[1]-=1
                answer+=dia*5+iron+stone
                break
            elif picks[2]>0:
                picks[2]-=1
                answer+=dia*25+iron*5+stone
                break
    
    return answer
            