n=int(input())
arr=list(map(int,input().split()))
x=int(input())
ans=0
a,b=0,n-1
arr.sort()
while a<b:
    if arr[a]+arr[b]==x:
        ans+=1
    if arr[a]+arr[b]<x:
        a+=1
        continue
    b-=1
print(ans)
