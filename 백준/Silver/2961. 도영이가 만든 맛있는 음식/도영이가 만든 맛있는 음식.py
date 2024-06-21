import sys

n= int(sys.stdin.readline())
arr=[]
for i in range(n):
    s,t = map(int,sys.stdin.readline().split())
    arr.append((s,t))
combination=[]
def c(index,result,r):
    if index==len(arr):
        if r==len(result):
            combination.append(result[:])
        return
    result.append(arr[index])
    c(index+1,result,r)
    result.pop()
    c(index+1,result,r)

for i in range(1,len(arr)+1):
    c(0,[],i)

minGap= sys.maxsize
for i in combination:
    sAnswer =0
    tAnswer =0
    for (ss,tt) in i:
        if sAnswer==0 and tAnswer==0:
            sAnswer+=ss
            tAnswer+=tt
        else:
            sAnswer*=ss
            tAnswer+=tt
    if minGap>abs(sAnswer-tAnswer):
        minGap=abs(sAnswer-tAnswer)
print(minGap)
