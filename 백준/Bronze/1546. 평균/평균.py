import sys

n= int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))

m=max(arr)

new=[]
for i in arr:
    k=i/m*100
    new.append(k)
s=sum(new)/n

print(s)