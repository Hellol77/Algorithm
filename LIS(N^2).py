def print_IS(seq, x):
    for i in range(len(seq)):
        if x[i]: 
            print(seq[i], end="")
        else:
            print("_", end="")
    print()

def LIS_DP(seq):
    # code here
	L=[1] *len(seq)
	x=[0] *len(seq)
	for i in range(len(seq)):
		for j in range(i):
			if seq[j]<seq[i]:
				L[i]=max(L[j]+1,L[i])
	res=max(L)
	for i in range(len(seq)-1,-1,-1):
		if L[i]==res:
			x[i]=1
			res-=1
	return max(L),x

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
print_IS(seq,x)
print(lis)
