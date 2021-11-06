def solve(A):
	S =[[0 for col in range(len(A)+1)] for row in range(201)]
	for x in range(1,len(A)+1):
		for k in range(1,201):
			T=S[1][x-1]
			for t in range(1,k+1):
				if T>S[t][x-1]:
					T=S[t][x-1]
			S[k][x]=T+abs(A[x-1]-k)
	L=S[1][len(A)]
	for p in range(1,201):
		if L>S[p][len(A)]:
			L=S[p][len(A)]
	return L
A=[int(x) for x in input().split()]
print(solve(A))
# 오른차순으로 만들기(같아도 된다.)
# 1<= n <=1000
# 1<= 정수 값 <= 200
# 출력은 오름차순이 되기 위해 필요한 연산의 최소 횟수
# 입력할때 숫자사이마다 공백을 입력한다.