def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1] # 먼곳먼저 간다.
    pickups = pickups[::-1]
    answer = 0
    
    d = 0
    p = 0
    
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:
            d -= cap # 가면서 주고 오면서 가져가기 때문에 d,p 둘 다 한꺼번에 빼준다.
            p -= cap
            answer += (n - i) * 2
    return answer