import sys
sys.setrecursionlimit(1000001)

from collections import defaultdict

A = defaultdict(list)
visited = [False] *100001

def dfs(u):
    visited[u] = True
    if not A[u]:
        return 1,0
    on, off=1,0
    for v in [v for v in A[u] if not visited[v]]:
        child_on, child_off = dfs(v)
        on+=min(child_on,child_off)
        off+=child_on
    return on,off
    

def solution(n, lighthouse):
    for u,v in lighthouse:
        A[u].append(v)
        A[v].append(u)
    on,off = dfs(1)
    return min(on,off)



