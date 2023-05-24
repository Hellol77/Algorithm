def solution(targets):
    answer=0
    targets.sort(key=lambda x:x[1])
    temp=0
    for target in targets:
        if temp<=target[0]:
            answer+=1
            temp=target[1]
    return answer