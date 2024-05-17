def solution(rows, columns, queries):
    arr= [ [0 for i in range(columns)]for i in range(rows) ]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = ((i) * columns + j+1) 
    realanswer=[]
    for query in queries:
        
        query = [ i -1 for i in query]
        temp = arr[query[0]][query[1]]
        answer=temp
        # 좌측
        for i in range(query[0]+1,query[2]+1):
            arr[i-1][query[1]] = arr[i][query[1]]
            answer=min(answer, arr[i][query[1]])
            
        # 하단
        for i in range(query[1]+1,query[3]+1):
            arr[query[2]][i-1]=arr[query[2]][i]
            answer=min(answer, arr[query[2]][i])
        # 우측
        for i in range(query[2]-1,query[0]-1,-1):
            arr[i+1][query[3]]=arr[i][query[3]]
            answer=min(answer,arr[i][query[3]])
        # 상단
        for i in range(query[3]-1,query[1]-1,-1):
            arr[query[0]][i+1] = arr[query[0]][i]
            answer=min(answer,arr[query[0]][i])
        
        arr[query[0]][query[1]+1]=temp
        realanswer.append(answer)
    return realanswer
        
            