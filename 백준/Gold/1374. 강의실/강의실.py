import sys
import heapq

n=int(sys.stdin.readline())
h=[]
q=[] # 끝나는 시간만 넣는 힙
count=0
for i in range(n):
    h.append(list(map(int,sys.stdin.readline().split())))

h.sort(key=lambda x:x[1])

for i in h:
    while q and q[0]<=i[1]:
        heapq.heappop(q)
    heapq.heappush(q, i[2])
    count=max(count,len(q))

print(count)
        