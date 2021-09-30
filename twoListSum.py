def two_sum(X,Y,t):
	i = len(X)-1
	j=len(Y)-1
	while i !=-1 and j!=-1:
		if -t==X[i]+Y[j]:
			return True
		elif i==0:
			j=j-1
		elif j==0:
			i=i-1
		elif X[i]-X[i-1]>Y[j]-Y[j-1]:
			j=j-1
		elif X[i]-X[i-1]<Y[j]-Y[j-1]:
			i=i-1
		else:
			i=i-1
	return False

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

A.sort()
B.sort()
temp=0
for i in C:
	if two_sum(A,B,i):
		temp=1
		print("True")
		break
if temp==0:
	print("False")