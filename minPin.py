n=int(input())
A=[]
for i in range(n):  #O(n)=n
	f,s=map(int,input().split())
	A.append((f,s))
A.sort(key=lambda x:(x[1])) 
k=A[0][1]
result=1
for i in range(n):
	if A[i][0]>k:
		k=A[i][1]
		result+=1
print(result)
# 최소못의 개수찾기