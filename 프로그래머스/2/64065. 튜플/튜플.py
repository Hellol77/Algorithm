def solution(s):
    s = s[2:len(s)-2]
    arr = s.split("},{")
    temp=[]
    answer=[]
    for i in arr:
        temp.append(i.split(','))
    temp.sort(key=len)
    t=set()
    for i in temp:
        ss = set(i)
        answer.append(int("".join(list(ss-t))))
        t=ss
    return answer
            