def solution(today, terms, privacies):
    dic={}
    todayArr=today.split('.')
    todayArr=list(map(int,todayArr))
    answer=[]
    for i in terms:
        tArr=i.split(' ')
        dic[tArr[0]]=int(tArr[1])
        
    for index,i in enumerate(privacies,start=1):
        arr=i.split(' ')
        dateArr=arr[0].split('.')
        dateArr=list(map(int,dateArr))
        t=arr[1]
        dateArr[1]+=dic[t]
        expiredDate=dateArr[0]*(28*12)+dateArr[2]+(dateArr[1])*28
        todayDate=todayArr[0]*(28*12)+todayArr[2]+(todayArr[1])*28
        if expiredDate<=todayDate:
            answer.append(index)
            continue
    
    return answer