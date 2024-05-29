def solution(s):
    answer=[]
    for i in range(1,len(s)+1):
        a = ""
        count = 1
        temp = s[:i]
        for j in range(i,len(s)+i,i):
            if temp == s[j:j+i]:
                count+=1
            else:
                if count!=1:
                    a=a+str(count)+temp
                else:
                    a=a+temp
                temp=s[j:j+i]
                count=1
        answer.append(len(a))
        
    return min(answer)