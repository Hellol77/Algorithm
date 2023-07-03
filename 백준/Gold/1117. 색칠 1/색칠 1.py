import sys

w, h, f, c, x1, y1, x2, y2= map(int,sys.stdin.readline().split())

xx = w-f
if xx <w//2:
	xx=w-xx
spiltY = c+1
total = w*h
splitX = w-xx

n=x2-x1 # 만약 x가 splitX보다 클 경우 그대로. 접어도 겹치는 부분이 없으므로
if x1<splitX:
	if x2<=splitX:
		n*=2
	elif x2>splitX:
		n+=splitX-x1
		
print(total - (n*(y2-y1)*spiltY))