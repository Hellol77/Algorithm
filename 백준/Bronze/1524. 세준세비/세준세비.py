import sys

t = int(sys.stdin.readline())
for i in range(t) :
    input()	
    N, M = map(int, input().split())
    sj = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    sb = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    
    while sj and sb :	
        if sj[-1] >= sb[-1] :	
            sb.pop()
        else :
            sj.pop()
    
    if sj :
        print('S')
    elif sb :
        print('B')
    else :
        print('C')