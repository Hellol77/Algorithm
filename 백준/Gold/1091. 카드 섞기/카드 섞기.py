import sys

n=int(sys.stdin.readline())
P=list(map(int,sys.stdin.readline().split()))
realP=P
S=list(map(int,sys.stdin.readline().split()))

G=[0,1,2]*(n//3)
new=[0]*n
answer=0

while P!=G:
    for i in range(n):
        new[S[i]]=P[i]
        
    P = new
    new=[0]*n
    answer+=1
    if realP == P:
        answer=-1
        break
print(answer)