def solution(rows, columns, queries):
    arr= [ [0 for i in range(columns)]for i in range(rows) ]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = ((i) * columns + j+1) 
    print(arr)