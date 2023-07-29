import sys

n,m=map(int,sys.stdin.readline().split())

def gcd(a,b):
    mod=a%b
    while mod>0:
        a=b
        b=mod
        mod=a%b
    return b
    
print('1'*gcd(n,m))