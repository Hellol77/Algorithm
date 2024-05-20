def solution(clothes):
    d={}
    answer=1
    for i in clothes:
        if not i[1] in d:
            d[i[1]]=[i[0]]
        else:
            d[i[1]].append(i[0])
    for i in d.values():
        answer *= len(i)+1
    return answer-1