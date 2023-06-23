n,c,w=map(int,input().split())
arr=[]
for i in range(n):
    temp=int(input())
    arr.append(temp)
maxnum=max(arr)
answer=0
for i in range(1,maxnum+1):
    money=0
    for j in arr:
        count,remain=divmod(j,i)
        if remain:
            expense=c*count
        else:
            expense=c*(count-1)
        target=(count*i*w) - expense
        if target<0:
            continue
        money+=target
    if answer<=money:
        answer=money
        
print(answer)
        
    
