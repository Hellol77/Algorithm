def solution(storey):
    answer=[]
    def func(st,count):
        
        if st == 0:
            answer.append(count)
            return
        
        k=10-st%10
        o=st%10
        if k < o:
            func(st//10+1,count+(k))
        elif k > o:
            func(st//10,count+o)
        else:
            func(st//10,count+o)
            func(st//10+1,count+o)
            
    
    func(storey,0)
    return min(answer)