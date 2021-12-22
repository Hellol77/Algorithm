from heapq import *

f=[int(x) for x in input().split()]
n=len(f)
T=[]
for i in range(n):
	heappush(T,(f[i],str(i)))
while len(T)>1:
	a=heappop(T)
	b=heappop(T)
	heappush(T,(a[0]+b[0],"("+a[1]+" "+b[1]+")"))
	
tree_string=heappop(T)[1]
bit=[0]*n
tree_string=tree_string.split()
d=0
for i in tree_string:
	for j in range(len(i)):
		if i[j]=="(":
			d+=1
		elif i[j]==")":
			d-=1
		else:
			if i[j-1]=="(":
				a=int(i[j:])
				bit[a]=d
				continue
			elif j+1==len(i):
				break
			elif i[j+1]==")":
				a=int(i[0:j+1])
				bit[a]=d
				continue
			else:
				continue
result=0
for i in range(n):
	result+=bit[i]*f[i]
print(result)