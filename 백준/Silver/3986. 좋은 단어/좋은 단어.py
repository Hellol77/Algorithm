n=int(input())
answer=0
for i in range(n):
    text=input()
    stack=[]
    for j in range(len(text)):
        if stack:
            if stack[-1]==text[j]:
                stack.pop()
            else:
                stack.append(text[j])
            
        else:
            stack.append(text[j])
    if not stack:
        answer+=1    
print(answer)