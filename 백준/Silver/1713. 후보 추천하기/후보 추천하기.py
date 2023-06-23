n=int(input())
r=int(input())
arr=list(map(int,input().split()))
dic={}
answer=[]
for i in arr:

    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
    if len(answer)==n:
        if i in answer:
            continue
        minR=1001
        for j in answer:
            if minR>dic[j]:
                minR=dic[j]
                
        temp=answer[:]
        
        for index,k in enumerate(temp):
            if dic[k]==minR:
                answer.remove(k)
                dic[k]=0
                answer.append(i)
                break
    else:
        if i in answer:
            continue
        answer.append(i)
answer.sort()
for i in answer:
    print(i,end=' ')