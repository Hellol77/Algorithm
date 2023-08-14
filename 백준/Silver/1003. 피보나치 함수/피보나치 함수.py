import sys

zero=[1,0,1]
one=[0,1,1]
def f(num):
    global zero,one
    
    if len(zero)<=num:
        for i in range(len(zero),num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[num],one[num]))
    
    
n=int(sys.stdin.readline())
for i in range(n):
    f(int(sys.stdin.readline()))