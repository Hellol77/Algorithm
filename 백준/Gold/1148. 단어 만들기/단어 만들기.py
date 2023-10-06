import sys

wordList=[]
board=[]
while True:
    k=sys.stdin.readline().rstrip()
    if k=='-':
        break
    wordList.append(k)
    
    
while True:
    k=sys.stdin.readline().rstrip()
    if k=='#':
        break
    board.append(k)
  
def solve(puzzle):
    answer={}
    dic={}
    for i in puzzle:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for onepuzzle in puzzle:
        count=0
        for word in wordList:
            flag=True
            temp=dic.copy()
            if onepuzzle in word:
                for alpa in word:
                    if alpa in puzzle and temp[alpa]>0:
                        temp[alpa]-=1
                    else:
                        flag=False
                        break
                if flag==False:
                    continue
                elif flag==True:
                    count+=1
            elif onepuzzle not in word:
                continue
        answer[onepuzzle]=count
        
        
    minCount = min(answer.values())
    maxCount=max(answer.values())

    maxarr=[]
    minarr=[]
    
    for key,val in answer.items():
        if val == minCount:
            minarr.append(key)
        if val == maxCount:
            maxarr.append(key)
    print(''.join(sorted(minarr)),end=' ')
    print(minCount,end=' ')
    print(''.join(sorted(maxarr)),end=' ')
    print(maxCount)
                
            
for i in board:
    solve(i)

    
