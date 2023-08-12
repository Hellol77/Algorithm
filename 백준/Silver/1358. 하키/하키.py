import sys

W,H,X,Y,P=map(int,sys.stdin.readline().split())
count=0

for i in range(P):
    x,y=map(int,sys.stdin.readline().split())
    
    if X<=x<=X+W and Y<=y<=Y+H:
        count+=1
        continue
    r=H/2
    d1=((x-X)**2+(y-(Y+r))**2)**0.5
    d2=((x-(X+W))**2+(y-(Y+r))**2)**0.5
    if d1<=r or d2 <=r:
        count+=1
        
print(count)