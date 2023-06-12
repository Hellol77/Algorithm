def solution(weights):
    answer=0
    dic={}
    for i in weights:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    
    
    for i in dic:
        if dic[i]>1:
            answer+=(dic[i]*(dic[i]-1))/2
        if i*2/3 in dic:
            answer+=dic[i*(2/3)]*dic[i]
        if i*2/4 in dic:
            answer+=dic[i*(2/4)]*dic[i]
        if i*3/4 in dic:
            answer+=dic[i*(3/4)]*dic[i]
    return answer
            
        