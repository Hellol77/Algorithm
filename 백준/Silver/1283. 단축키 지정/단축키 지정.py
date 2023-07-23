import sys

n=int(sys.stdin.readline())

dic={}
arr=[]
for i in range(n):
    flag=0
    letter = list(map(str,sys.stdin.readline().rstrip().split()))
    
    
    for j in range(len(letter)):
        if letter[j][0].upper() not in dic:
            dic[letter[j][0].upper()]=1
            temp=letter[j].replace(letter[j][0],'['+letter[j][0]+']',1)
            letter[j]=temp
            k=' '.join(letter)
            arr.append(k)
            flag=1
            break
    if flag!=1:
        letter2=" ".join(letter)
        for i in letter2:
            if  i !=' ' and i.upper() not in dic:
                dic[i.upper()]=1
                letter2=letter2.replace(i,'['+i+']',1)
                flag=1
                arr.append(letter2)
                break
    if flag!=1:
        k=' '.join(letter)
        arr.append(k)
        
            
        
        
for i in arr:
    print(i)