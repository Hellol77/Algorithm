from collections import deque
n=int(input())
arr=[i for i in range(1,n+1)]
dq=deque(arr)

while 1:
    if len(dq)==1:
        print(dq[0])
        break
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        break
    k=dq.popleft()
    dq.append(k)
    
    