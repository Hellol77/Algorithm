def solution(beginning, target):
    row,col = len(beginning),len(beginning[0])
    arr = [[1 if beginning[i][j] != target[i][j] else 0 for j in range(col)] for i in range(row)]
    
    mini = 1000000
    baseRow = arr[0]
    
    for r in arr:
        diff = 0
        for otherRow in arr:
            if r == otherRow: continue
            tempRow = [1-i for i in otherRow]
            if r == tempRow:
                diff+=1
                continue
            return -1
        diff+=sum(r)
        if diff < mini:
            baseRow=r
            mini = diff
    return mini