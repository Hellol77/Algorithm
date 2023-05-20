def solution(babbling):
    count=0
    text=["aya", "ye", "woo", "ma" ]
    for i in babbling:
        for j in text:
            if j *2 not in i:
                i=i.replace(j,' ')
        if i.strip()=='':
            count+=1   
    return count
        