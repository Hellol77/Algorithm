def max_sum(A):
	# 최대 구간 합 리턴
	P=[]
	P.append(A[0])
	for i in range(1,len(A)):
		P.append(P[i-1]+A[i])
	t=A[0]
	for i in range(0,len(A)-1):
		for j in range(i,len(A)):
			if i ==0:
				if t<P[j]:
					t=P[j]
			if i!=0 and t<=P[j]-P[i-1]:
				t=P[j]-P[i-1]
	return t
A = [int(x) for x in input().split()]
sol = max_sum(A)
print(sol)