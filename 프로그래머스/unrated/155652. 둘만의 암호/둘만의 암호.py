from string import ascii_lowercase
def solution(s, skip, index):
    
    arr=list(ascii_lowercase)
    answer=''
    for i in skip:
        arr.remove(i)
    for i in s:
        tempIndex=index
        iIndex=arr.index(i)
        temp=arr[iIndex]
        while tempIndex!=0:
            iIndex=(iIndex+1)%len(arr)
            temp=arr[iIndex]
            tempIndex-=1
        answer+=temp
    return answer
        
