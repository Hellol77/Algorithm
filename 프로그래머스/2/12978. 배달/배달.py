import heapq

def dijkstra(dist,a):
    heap=[]
    heapq.heappush(heap,[0,1])
    while heap:
        cost, node = heapq.heappop(heap)
        for c,n in a[node]:
            if cost+c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(heap,[cost+c,n])
                
        
def solution(N, road, K):
    dist = [float('inf')] * (N+1)
    dist[1] =0 
    a = [[] for i in range(N+1)]
    for r in road:
        a[r[0]].append([r[2],r[1]])
        a[r[1]].append([r[2],r[0]])
    dijkstra(dist,a)
    return len([i for i in dist if i<=K])
        
        
    
    