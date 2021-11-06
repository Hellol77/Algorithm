def solve(A):
	global result
	k=0
	c=0
	total=0
	if len(A)==1:
		return A[0]
	m=min(A)
	min_index=A.index(m)
	if min_index==0:
		return m*len(A)+solve(A[min_index+1:])
	if min_index==len(A)-1:
		return m*len(A)+solve(A[:min_index])
	for i in range(1,len(A)+1):
		total+=i
	for i in range(1,len(A)-min_index):
		k+=i
	for i in range(1,min_index+1):
		c+=i
	return solve(A[:min_index])+m*(total-c-k)+solve(A[min_index+1:])


A=[int(x) for x in input().split()]
print(solve(A))
# 분할정복을 이용한 알고리즘
# 제일 값이 낮은 값을 잡고 왼쪽 인덱스부분과 오른쪽 인덱스 부분으로 나눈다
# 모든 인덱스 쌍읙 개수 - 왼쪽 부분의 개수와 오른쪽 부분의 인덱스 쌍 개수의 합 = 값이 낮은 값의 개수
# 제일 값이 낮은 값의 인덱스가 0이나 n-1일 경우 제일 낮은 값은 n개 있다.
