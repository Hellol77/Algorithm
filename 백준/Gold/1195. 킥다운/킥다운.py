import sys

s=sys.stdin.readline().rstrip()
l=sys.stdin.readline().rstrip()

answer=len(l)+len(s)

if len(l)<len(s):
    s,l=l,s
    
for i in range(len(s)):
    for j in range(i+1):
        if s[-1*(i+1)+j]=='2'and l[j]=='2':
            break
    else:
        answer=min(answer,len(l)+len(s)-(i+1))
        
    for j in range(i+1):
        if s[i-j]=='2'and l[len(l)-1-j]=='2':
            break
    else:
        answer=min(answer,len(l)+len(s)-(i+1))


for i in range(len(l)-len(s)):
    for j in range(len(s)):
        if s[j]=='2'and l[j+i]=='2':
            break
    else:
        answer=min(answer,len(l))
        
print(answer)