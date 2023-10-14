import sys

g=int(sys.stdin.readline())
a=0
b=1
arr=[]
answer=[]
for i in range(1,100001):
    arr.append(i)
    
while b<len(arr):
    if arr[b]**2-arr[a]**2 ==g:
        answer.append(b+1)
        b+=1
    elif arr[b]**2-arr[a]**2 >g:
        a+=1
    elif arr[b]**2-arr[a]**2<g:
        b+=1
    
if not answer:
    print(-1)
    
else: 
    for i in answer:
        print(i)
    

