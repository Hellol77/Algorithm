import sys

n=int(sys.stdin.readline())

answer=''
q=[]
for i in range(n):
    temp=False
    cmd,c,t = map(str,sys.stdin.readline().split())
    if cmd=='type':
        answer+=c
        q.append((int(t),answer))
    
    else:
        
        for i in range(len(q)-1,-1,-1):
            if q[i][0]>=int(t)-int(c):
                continue
            temp=True
            answer=q[i][1]
            q.append((int(t),answer))
            break
        if not temp:
            answer=''
            q.append((int(t),answer))
        
print(answer)
            
            