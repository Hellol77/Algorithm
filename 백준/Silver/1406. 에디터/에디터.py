import sys
arr1=list(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline())
arr2=[]
cursor= len(arr1)
for i in range(m):
    command=list(sys.stdin.readline().split())
    
    if command[0]=='P':
        arr1.append(command[1])
    elif command[0]=='L':
        if arr1:
            arr2.append(arr1.pop())
    elif command[0]=='D':
        if arr2:
            arr1.append(arr2.pop())
    else:
        if arr1:
            arr1.pop()
arr1.extend(reversed(arr2))        
print(''.join(arr1))