def solution(n, works):
    while n:
        max=0
        maxIndex=-1
        for index,i in enumerate(works):
            if max<i:
                max=i
                maxIndex=index
        n-=1
        if works[maxIndex]==0:
            continue
        works[maxIndex]-=1
    answer=0
    print(works)
    for i in works:
        if i==0:
            continue
        answer+=i*i
    return answer
        
                
    