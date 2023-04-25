n=int(input())

stack=[]
ans=[]
m=1
flag=1
for i in range(n):
    k=int(input())
    while m<=k:
        stack.append(m)
        ans.append('+')
        m+=1
    if stack[-1]==k:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        flag=0
        break
        
        
if flag==1:
    for i in ans:
        print(i)