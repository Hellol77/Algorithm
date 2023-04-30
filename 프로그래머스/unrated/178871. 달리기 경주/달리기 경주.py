def solution(players, callings):
    dic={i : player for i ,player in enumerate(players)}
    dic2=dict(map(reversed,dic.items()))
    for i in callings:
        loc=dic2[i] # 현재 등수
        loc2=loc-1
        i2=dic[loc2] # 앞 선수
        
        dic[loc]=i2
        dic[loc2]=i
        
        dic2[i]=loc2
        dic2[i2]=loc
        
    return list(dic.values())
        
        
        
    

    
