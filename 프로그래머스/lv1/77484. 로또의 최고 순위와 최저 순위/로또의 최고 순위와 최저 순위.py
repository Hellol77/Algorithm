def solution(lottos, win_nums):
    result = []
    answer=[]
    highCount = 7
    lowCount = 7
    for num in lottos:
        if num in win_nums:
            lowCount-=1
            highCount-=1
        elif num==0:
            highCount-=1
        else:
            continue
    result.append(highCount)
    result.append(lowCount)
    for i in result:
        if i==7:
            answer.append(6)
        else:  
            answer.append(i)
    return answer