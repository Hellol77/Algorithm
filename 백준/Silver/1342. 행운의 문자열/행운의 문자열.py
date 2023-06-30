import sys
arr=list(sys.stdin.readline().rstrip())

point = [0 for _ in range(26)]
char=set()
for i in arr:
    point[ord(i) - 97] += 1
    char.add(i)
        
answer=0

def solution (l,s):
    global answer
    if l==0:
        answer+=1
        return
    for i in char:
        if s!=i and point[ord(i) - 97] > 0 :
            point[ord(i) - 97] -= 1
            solution(l-1, i)
            point[ord(i) - 97] += 1

solution(len(arr), '')
print(answer)
        


