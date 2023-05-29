def solution(dartResult):
    arr=[]
    temp=''
    for index,i in enumerate(dartResult):
        if i.isdigit():                
            temp=str(temp)+str(i)
            continue
        elif i in ['S','D','T']:
            temp=int(temp)
            if i =='S':
                temp=temp**1
            elif i =='D':
                temp=temp**2
            elif i == 'T':
                temp=temp**3
        elif i == '*':
            if len(arr)>=1:
                arr[-1]=arr[-1]*2
            temp=temp*2
        elif i == '#':
            temp=temp*(-1)
        if index+1==len(dartResult) or dartResult[index+1].isdigit():
            arr.append(temp)
            temp=''
            continue
        if dartResult[index+1].isdigit():
            arr.append(temp)
            temp=''
    return sum(arr)
    
