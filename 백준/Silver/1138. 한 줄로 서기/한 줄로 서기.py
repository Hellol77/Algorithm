n=int(input())

arr=list(map(int,input().split()))
answer=[0 for i in range(n)]
for i in range(0,n):
    temp=arr[i]
    num=0
    # if answer[temp]==0:
    #     answer[temp]=i+1   
    for j in range(0,n): 
        if temp==num and answer[j]==0 :
            answer[j]=i+1
            break
        if answer[j]!=0:
            continue
        if answer[j]==0:
            num+=1
    # else:
    #     while answer[temp]!=0:
    #         temp+=1
    #     answer[temp]=i+1

        
for i in range(n):
    print(answer[i],end=' ')

    