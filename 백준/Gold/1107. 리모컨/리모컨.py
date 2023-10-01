import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
answer = abs(100-n)
if m:
    broken=list(sys.stdin.readline().split())
else:
    broken=[]
for i in range(1000001):
    for j in str(i):
        if j in broken:
            break
    else:
        answer=min(answer,len(str(i))+abs(i-n))
    


print(answer)

