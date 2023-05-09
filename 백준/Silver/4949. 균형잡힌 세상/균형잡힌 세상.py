while 1:
    text=input()
    stack=[]
    if text == '.':
        break
    for i in text:
        if i=='(' or i=='[':
            stack.append(i)
        
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')
                break
    if stack:
        print('no')
    if not stack:
        print('yes')
        

