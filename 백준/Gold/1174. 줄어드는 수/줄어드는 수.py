import sys

n=int(sys.stdin.readline())


answer=[]
def bt(c):
    answer.append(c)
    for i in range(0,int(str(c)[-1])):
        bt(int(str(c)+str(i)))
        

try:
    for i in range(10):
        bt(i)
    print(sorted(answer)[n-1])
    
except:
    print(-1)