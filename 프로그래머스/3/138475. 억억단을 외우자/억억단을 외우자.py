def divisors(num:int) -> list:
    divisors = [0] * (num + 1)
    for i in range(1,int(num ** 0.5) + 1):
        divisors[i*i]+=1
        for j in range(i * (i+1), num + 1, i):
            divisors[j]+=2
    return divisors


def solution(e, starts):
    max_num = e
    divisor_cnt = divisors(e)
    
    answer = [0] * (e+1)
    
    for i in range(e,0,-1):
        if divisor_cnt[i]>=divisor_cnt[max_num]:
            max_num = i
        answer[i]=max_num
        
    return [answer[s] for s in starts]
    
    
    
                
        

        
        