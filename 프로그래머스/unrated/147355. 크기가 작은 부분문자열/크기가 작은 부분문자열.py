def solution(t, p):
    answer=0
    strlen=len(p)
    for i in range(0,len(t)-strlen+1):
        if p>=t[i:i+strlen]:
            answer+=1
    return answer