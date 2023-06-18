def solution(n, arr1, arr2):
    answer=[]
    array1=[]
    array2=[]
    for i in arr1:
        bit=''
        for j in range(n-1,-1,-1):
            if i//(2**j) ==1:
                bit+='#'
                i=i%(2**j)
            else:
                bit+=' '
        array1.append(bit)
    for i in arr2:
        bit=''
        for j in range(n-1,-1,-1):
            if i//(2**j) ==1:
                bit+='#'
                i=i%(2**j)
            else:
                bit+=' '
        array2.append(bit)
    
    for i in range(n):
        temp=''
        for j in range(n):
            if array1[i][j] =='#' or array2[i][j] =='#':
                temp+=('#')
            elif array1[i][j] == ' ' and array2[i][j]== ' ':
                temp+=(' ')
        answer.append(temp)
                      
    return answer
        
        
        

    
        

    
        
            
            