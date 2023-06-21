r,c = map(int,input().split())
arr=[]
answer=[]
for i in range(r):
    temp=input()
    arr.append(temp)
for i in arr:
    temp=i.split('#')
    for j in temp:
        if len(j)>1:
            answer.append(j)
fliparr=list(map(list,zip(*arr)))
arr2=[]
for i in fliparr:
    temp=''.join(i)
    arr2.append(temp)
for i in arr2:
    temp=i.split('#')
    for j in temp:
        if len(j)>1:
            answer.append(j)

answer=[i for i in answer if i]
answer.sort()
print(answer[0])