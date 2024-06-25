import sys

n=int(sys.stdin.readline())

rows=[0]*n




answer=0

def promising(x):
    for i in range(x):
        if rows[x]==rows[i] or abs(x-i)==abs(rows[x]-rows[i]):
            return False
    return True


def q(x):
    global answer
    if x==n:
        answer+=1
        return

    else:
        for i in range(n):
            rows[x]=i
            if promising(x):
                q(x+1)

q(0)

print(answer)
