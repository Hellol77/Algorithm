def solution(record):
    result = []
    nameDic = {}
    answer=[]
    for i in record:
        temp=i.split(' ')
        if temp[0]=='Enter' or temp[0]=="Change":
            nameDic[temp[1]]=temp[2]
        result.append(temp)

    for i in result:
        if i[0] =='Enter':
            answer.append(f'{nameDic[i[1]]}님이 들어왔습니다.')
        elif i[0] == 'Leave':
            answer.append(f'{nameDic[i[1]]}님이 나갔습니다.')

    return answer