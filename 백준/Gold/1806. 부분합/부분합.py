import sys

n,s=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))

answer=sys.maxsize

l,r=0,0
temp=0
while True:
    if temp>=s:
        answer=min(answer,r-l)
        temp-=arr[l]
        l+=1
        
    elif r==n:
        break
    else:
        temp+=arr[r]
        r+=1
if answer==sys.maxsize:
    print(0)
else:
    print(answer)

        