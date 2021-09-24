import time, random
def evaluate_n2(A, x):
	t=0
	ans=0
	for i in range(len(A)):
		t+=A[i]
		for j in range(i):
			t*=x
		ans+=t
		t=0	
	return ans
def evaluate_n(A, x):
	t=A[len(A)-1]

	for i in range(len(A)-2,-1,-1):
		t=A[i]+x*t
	return t

random.seed()
n=int(input())
A=[]
for i in range(n):
	A.append(random.randint(-1000,1000))
x=random.randint(-1000,1000)




s=time.process_time()
evaluate_n2(A,x)
e=time.process_time()
print("수행시간 =",e-s)
s=time.process_time()
evaluate_n(A,x)
e=time.process_time()
print("수행시간 =",e-s)