import sys

n=int(sys.stdin.readline())
arr=[]

blue=0
white=0
for i in range(n):
    l=list(map(int,sys.stdin.readline().split()))
    arr.append(l)

def recursive(x,y,n):
    global blue,white
    s=0
    newLength = n//2
    for i in range(x,x+n):
        for j in range(y,y+n):
            s+=arr[i][j]

    if s==n*n:
        blue+=1
    elif s==0:
        white+=1
    else:
        recursive(x,y,newLength)
        recursive(x+newLength,y+newLength,newLength)
        recursive(x+newLength,y,newLength)
        recursive(x,y+newLength,newLength)

recursive(0,0,n)
print(white)
print(blue)
