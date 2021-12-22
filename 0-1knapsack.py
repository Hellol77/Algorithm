
k=int(input())
n=int(input())
S=list(map(int,input().split()))#용량
P=list(map(int,input().split()))#가격
MP=0
x=[0]*(n+1)
K=[]
for j in range(1,n+1):
	K.append((S[j-1],P[j-1],P[j-1]/S[j-1]))
K.sort(key=lambda x : -x[2])

def frac_knapsack(i, size):
	max_profit=0
	if i>n or size <=0:
		return max_profit	
	for l in range(len(K)):
		if size==0:
			break
		if size>K[l][0] and x[l+1]==0:
			max_profit+=K[l][1]
			size=size-K[l][0]
		elif size<=K[l][0] and x[l+1]==0:
			max_profit+=K[l][2]*size
			break
	return max_profit	
def knapsack(i,size):
	global MP
	if i>n or size<=0:
		return
	for k in range(i,n+1):
		x[k]=0	
	p=sum(K[j][1] for j in range(0,i-1) if x[j+1]==1)#가격의 합
	if K[i-1][0]<=size:
		B=frac_knapsack(i+1,size-K[i-1][0])
		if p+K[i-1][1]+B>MP:
			if p+K[i-1][1]>MP:
				MP=p+K[i-1][1]
			x[i]=1
			knapsack(i+1,size-K[i-1][0])
	B=frac_knapsack(i+1,size)
	
	if p+B >MP:
		x[i]=0
		knapsack(i+1,size)
knapsack(1,k)
print(MP)
