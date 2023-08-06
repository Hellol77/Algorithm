import datetime
import sys
n=list(map(int,sys.stdin.readline().split()))
m=list(map(int,sys.stdin.readline().split()))

start=datetime.date(n[0],n[1],n[2])
start1000=datetime.date(n[0]+1000,n[1],n[2])
end=datetime.date(m[0],m[1],m[2])

result1000=start1000-start
result=end-start

if result<result1000:
    print(f'D-{result.days}')
else:
    print('gg')