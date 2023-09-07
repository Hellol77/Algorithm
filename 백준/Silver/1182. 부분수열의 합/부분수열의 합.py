import sys

n,s = map(int,sys.stdin.readline().split())
arr = list(map(int, input().split()))
count = 0
def subset(i,tempSum):
    global count
    
    if i>=n:
        return
    tempSum+=arr[i]
    if tempSum==s:
        count+=1
    subset(i+1,tempSum)
    subset(i+1,tempSum-arr[i])
subset(0, 0)
print(count)
    
        
    