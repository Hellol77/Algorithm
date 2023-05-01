def solution(id_list, report, k):
    answer=[[] for i in range(len(id_list))]
    realAnswer=[0 for i in range(len(id_list))]
    reportNum=dict.fromkeys(id_list,0)
    reportDic={}
    answer=dict.fromkeys(id_list,0)
    realAnswer=[]
    for i in report:
        if i in reportDic:
            continue
        reportDic[i]=0
        arr=i.split(' ')
        reportNum[arr[1]]+=1
        
    for i in reportDic.keys(): # 신고한 사람 이름 찾기
        temp=i.split(' ')
        if reportNum[temp[1]]>=k:
            answer[temp[0]]+=1
    for i in id_list:
        realAnswer.append(answer[i])
    return realAnswer