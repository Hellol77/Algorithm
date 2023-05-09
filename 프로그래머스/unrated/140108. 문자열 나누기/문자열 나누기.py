def solution(s):
    answer=0
    start=0
    t=0
    temp=s[0]
    for index,i in enumerate(s):
        if index==len(s)-1:
            answer+=1
            break
        if temp==i:
            start+=1
        else:
            t+=1
        if start==t:
            answer+=1
            temp=s[index+1]
            start=0
            t=0
    return answer