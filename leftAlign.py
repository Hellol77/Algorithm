W = int(input())
words = input().split()
# code below
D=[0]*(len(words)+1)

for i in range(1,len(words)+1):
	cw=0
	min_penalty=99999999
	j=i
	while j>0:
		cw+=len(words[j-1])+1
		if cw -1>W:
			break
		cp=D[j-1]+(W-cw+1)**3
		if min_penalty>cp:
			min_penalty=cp
		j=j-1
	D[i]=min_penalty
print(D[len(words)])