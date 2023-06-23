n,m=map(int,input().split())
qArr=list(map(int,input().split()))
kArr=list(map(int,input().split()))
pArr=list(map(int,input().split()))

arr=[[0 for i in range(n+1)] for j in range(m+1)]

q=qArr[0]
qArr.remove(q)

k=kArr[0]
kArr.remove(k)

p=pArr[0]
pArr.remove(p)

positionQ=[]
positionK=[]
positionP=[]

x=0
y=0


for i in range(len(arr)):
    arr[i][0]='p'
for i in range(len(arr[0])):
    arr[0][i]='p'
if q!=0:

    for i in qArr:
        if x==0:
            x=i
            continue
        if y==0:
            y=i
            arr[y][x]='q'
            positionQ.append((x,y))
            x=0
            y=0
x=0
y=0

if k!=0:     
    for i in kArr:
        if x==0:
            x=i
            continue
        if y==0:
            y=i
            arr[y][x]='k'
            positionK.append((x,y))
            x=0
            y=0
x=0
y=0

if p!=0:
    for i in pArr:
        if x==0:
            x=i
            continue
        if y==0:
            y=i
            arr[y][x]='p'
            positionP.append((x,y))
            x=0
            y=0
if p!=0:            
    for x,y in positionP:
        arr[y][x]=='p'
if q!=0:
    for x,y in positionQ:
        tempx=x
        tempy=y
        while 1: # 윗 왼쪽 대각선
            
            if tempy-1<0 or tempx-1<0: 
                break
            else:
                if arr[tempy-1][tempx-1]!='k' and arr[tempy-1][tempx-1]!='p' and arr[tempy-1][tempx-1]!='q' :
                    arr[tempy-1][tempx-1]='x'
                    tempx-=1
                    tempy-=1
                else:
                    break
        
        tempx=x
        tempy=y
        while 1: # 윗 오른쪽 대각선
            
            if tempy-1<0 or tempx+1>=len(arr[0]): 
                break
            else:
                if arr[tempy-1][tempx+1]!='k' and arr[tempy-1][tempx+1]!='p' and arr[tempy-1][tempx+1]!='q':
                    arr[tempy-1][tempx+1]='x'
                    tempx+=1
                    tempy-=1
                else:
                    break
        tempx=x
        tempy=y
        while 1: # 아래 오른쪽 대각선
            
            if tempy+1>=len(arr) or tempx+1>=len(arr[0]): 
                break
            else:
                if arr[tempy+1][tempx+1]!='k' and arr[tempy+1][tempx+1]!='p'and arr[tempy+1][tempx+1]!='q' :
                    arr[tempy+1][tempx+1]='x'
                    tempx+=1
                    tempy+=1
                else:
                    break
                    
        tempx=x
        tempy=y
        while 1: # 아래 왼쪽 대각선
            
            if tempy+1>=len(arr) or tempx-1<0: 
                break
            else:
                if arr[tempy+1][tempx-1]!='k' and arr[tempy+1][tempx-1]!='p'and arr[tempy+1][tempx-1]!='q' :
                    arr[tempy+1][tempx-1]='x'
                    tempx-=1
                    tempy+=1
                else:
                    break
                        
        # for i in range(len(arr)):
        #     if arr[i][tempx] =='k' or arr[i][tempx]=='p':
        #         break
        #     elif arr[i][tempx]=='q':
        #         continue
        #     else:
        #         arr[i][tempx]='x'
                
        # for i in range(len(arr[0])):
        #     if arr[tempy][i] =='k' or arr[tempy][i]=='p':
        #         break
        #     elif arr[tempy][i]=='q':
        #         continue
        #     else:
        #         arr[tempy][i]='x'
        tempx=x
        tempy=y
        while 1: 
            
            if tempy+1>=len(arr):
                break
            else:
                if arr[tempy+1][tempx]!='k' and arr[tempy+1][tempx]!='p' and arr[tempy+1][tempx]!='q':
                    arr[tempy+1][tempx]='x'
                    tempy+=1
                else:
                    break
        tempx=x
        tempy=y
        while 1: 
            
            if tempy-1<0:
                break
            else:
                if arr[tempy-1][tempx]!='k' and arr[tempy-1][tempx]!='p'and arr[tempy-1][tempx]!='q' :
                    arr[tempy-1][tempx]='x'
                    tempy-=1
                else:
                    break                    
        tempx=x
        tempy=y
        while 1: 
            
            if tempx+1>=len(arr[0]):
                break
            else:
                if arr[tempy][tempx+1]!='k' and arr[tempy][tempx+1]!='p'and arr[tempy][tempx+1]!='q' :
                    arr[tempy][tempx+1]='x'
                    tempx+=1
                else:
                    break
        tempx=x
        tempy=y
        while 1: 
            
            if tempx-1<0:
                break
            else:
                if arr[tempy][tempx-1]!='k' and arr[tempy][tempx-1]!='p' and arr[tempy][tempx-1]!='q' :
                    arr[tempy][tempx-1]='x'
                    tempx-=1
                else:
                    break  
if k!=0:    
    for x,y in positionK:
        tempx=x
        tempy=y
        if tempx+2<len(arr[0]):
            if tempy+1<len(arr):
                arr[tempy+1][tempx+2]='x'
            if tempy-1>=0:
                arr[tempy-1][tempx+2]='x'
        tempx=x
        tempy=y
        if tempx+1<len(arr[0]):
            if tempy+2<len(arr):
                arr[tempy+2][tempx+1]='x'
            if tempy-2>=0:
                arr[tempy-2][tempx+1]='x'
                
        tempx=x
        tempy=y
        if tempx-2>=0:
            if tempy+1<len(arr):
                arr[tempy+1][tempx-2]='x'
            if tempy-1>=0:
                arr[tempy-1][tempx-2]='x'
                
        tempx=x
        tempy=y
        if tempx-1>=0:
            if tempy+1<len(arr):
                arr[tempy+2][tempx-1]='x'
            if tempy-1>=0:
                arr[tempy-2][tempx-1]='x'
            

    
answer=0
for i in arr:
   answer+= i.count(0)

print(answer)
                
                
    
    
    