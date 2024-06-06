def solution(n, t, m, p):
    answer=''
    temp=''
    for i in range(t*m):
        temp+=convert(i,n)
    while len(answer)<t:
        answer+=temp[p-1]
        p+=m
    return answer
        

def convert (num,digit):
    temp='0123456789ABCDEF'
    q,r = divmod(num,digit)
    
    if q==0:
        return temp[r]
    else:
        return convert(q,digit)+temp[r]
        
    