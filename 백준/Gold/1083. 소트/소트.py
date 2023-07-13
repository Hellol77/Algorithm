import sys

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
s=int(sys.stdin.readline())

for i in range(n-1):
    if s==0:
        break
    maxx,index=arr[i],i
    for j in range(i+1,min(n,i+1+s)):
        if maxx<arr[j]:
            maxx=arr[j]
            index=j
    s-=index-i
    for k in range(index,i,-1):
        arr[k]=arr[k-1]
    arr[i]=maxx
print(*arr)