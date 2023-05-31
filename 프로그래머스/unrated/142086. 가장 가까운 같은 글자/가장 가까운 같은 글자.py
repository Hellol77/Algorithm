def solution(s):
    dic={}
    arr=[]
    for index,i in enumerate(s):
        if i in dic:
            arr.append(index-dic[i])
            dic[i]=index
        elif i not in dic:
            dic[i]=index
            arr.append(-1)
            
    return arr
        