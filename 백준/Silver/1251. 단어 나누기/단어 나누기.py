s=list(input())
answer=[]
temp=[]
for i in range(1,len(s)-1):
    for j in range(i+1,len(s)):
        a=s[0:i]
        b=s[i:j]
        c=s[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        temp.append(a+b+c)
for i in temp:
    answer.append(''.join(i))
    
print(sorted(answer)[0])