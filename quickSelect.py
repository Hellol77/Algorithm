def QuickSelect(A,k):
    p=A[0]
    S=[]
    M=[]
    L=[]
    for i in A:
        if i<p:
            S.append(i)
        elif i>p:
            L.append(i)
        else:
            M.append(i)
    if len(S)>=k:
        return QuickSelect(S,k)
    elif len(S)+len(M)<k:
        return QuickSelect(L,k-len(S)-len(M))
    else:
        return p
    
    
    
    
n,k=map(int,input().split())

T=list(map(int,input().split()))

print(QuickSelect(T,k))