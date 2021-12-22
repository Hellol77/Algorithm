n=int(input())
A=[]
F=[0 for i in range(200001)]
S=[0 for i in range(200001)]
for i in range(n):  #O(n)=n
	f,s=map(int,input().split())
	F[f]+=1
	S[s]+=1
	A.append((f,s))
A.sort(key=lambda x:(x[1])) 
max_S=A[-1][1]
D=[0 for i in range(A[-1][1]+1)]
D[max_S]=S[max_S]
for i in range(max_S,0,-1):
	if i==max_S:
		D[i]=S[i]
	else:
		D[i]=D[i+1]+S[i]-F[i+1]
print(max(D))

#하나의 핀으로 관통할 수 있는 막대의 최대개수 구하기