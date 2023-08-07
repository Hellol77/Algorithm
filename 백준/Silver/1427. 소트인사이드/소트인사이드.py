import sys

n=list(sys.stdin.readline().rstrip())

n.sort(reverse=True)
''.join(n)
print(int(''.join(n)))