import time, random
def evaluate_n2(A, x):
# code for O(n^2)-time function
	temp=0
	answer=0
	for i in range(len(A)):
		temp+=A[i]
		for j in range(i):
			temp*=x
		answer+=temp
		temp=0	
	return answer
def evaluate_n(A, x):
# code for O(n)-time function
	B=[]
	sqx=x**len(A)
	for i in A:
		B.append(i*sqx)
	for i in range(len(A)):
		temp=0
		
		
	# eachResult=[]
	# answer=0
	# k=0
	# for i in A:
	# 	eachResult.append(i*(x**k))
	# 	k+=1
	# for i in eachResult:
	# 	answer+=i
	# return answer
random.seed()# random 함수 초기화
n=int(input())
A=[]
for i in range(n):
	A.append(random.randint(-1000,1000))
x=random.randint(-1000,1000)



# n 입력받음
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
# evaluate_n2 호출
# evaluate_n 호출
# 두 함수의 수행시간 출력
s=time.process_time()
evaluate_n2(A,x)
e=time.process_time()
print("수행시간 =",e-s)
s=time.process_time()
evaluate_n(A, x)
e=time.process_time()
print("수행시간 =",e-s)
