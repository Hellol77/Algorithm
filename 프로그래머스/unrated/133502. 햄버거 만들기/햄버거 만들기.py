def solution(ingredient):
    arr=[]
    answer=0
    temp=0
    for i in ingredient:
        arr.append(i)
        if arr[-4:]==[1,2,3,1]:
            answer+=1
            for i in range(4):
                arr.pop()
    return answer