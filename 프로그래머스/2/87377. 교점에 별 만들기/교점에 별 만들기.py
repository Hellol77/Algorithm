from itertools import combinations
def calculation(line1,line2):
    a,b,e=line1
    c,d,f=line2
    
    if a*d == b*c:
        return
    x=(b*f-e*d)/(a*d-b*c) 
    y=(e*c-a*f)/(a*d-b*c)
    
    if x==int(x) and y==int(y):
        return [int(x),int(y)]

def solution(line):
    points = []
    for line1,line2 in combinations(line,2):
        point = calculation(line1,line2)
        if point:points.append(point)
        
    x1,x2= min(points,key=lambda x:x[0])[0],max(points,key=lambda x:x[0])[0]+1
    y1,y2= min(points,key=lambda x:x[1])[1],max(points,key=lambda x:x[1])[1]+1
    answer = [ ["." for i in range(x2-x1)] for i in range(y2-y1) ]
    for x,y in points:
        answer[y-y1][x-x1] = '*'
    answer.reverse()
    return [''.join(a) for a in answer]
    
    
    
    
    
    
    