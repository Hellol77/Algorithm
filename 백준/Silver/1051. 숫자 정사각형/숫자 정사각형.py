n,m = map(int,input().split())
arr=[]
for i in range(n):
    temp=input()
    arr.append(temp)
    
if n>=m:
    A=n
answer=1
for i in range(n):
    for j in range(m):
        temp=0
        while 1:
            if i+temp<n and j+temp<m:
                if arr[i][j]==arr[i+temp][j] ==arr[i][j+temp]==arr[i+temp][j+temp]:
                    if answer<temp+1:
                        answer=temp+1
                temp+=1
            else:
                break
        
                
print(answer*answer)