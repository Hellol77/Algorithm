import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    start,end = map(int,sys.stdin.readline().split())
    arr.append((start,end))

arr.sort(key=lambda x:(x[1],x[0]))
nowEnd=-1
answer=0
for i in range(n):
    if nowEnd<=arr[i][0]:
        nowEnd=arr[i][1]
        answer+=1


print(answer)
