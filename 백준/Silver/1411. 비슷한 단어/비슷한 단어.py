import sys

n=int(sys.stdin.readline())
arr=[[]for i in range(101)]
dic=[{}for i in range(101)]
for i in range(n):
    num=0
    m=str(sys.stdin.readline().rsplit())
    
    for j in m:
        if j not in dic[i]:
            dic[i][j]=str(num)
            num+=1
        arr[i]+=dic[i][j]
        
answer=0        
for i in range(n):
    for j in range(i+1 ,n):
        if arr[i]==arr[j]:
            answer+=1
print(answer)