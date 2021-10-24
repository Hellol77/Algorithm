def merge(A, first, mid1,mid2,last):
    # i <= j and j < k <= l
    # 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수

    i=first
    j=mid1+1
    k=mid2+1
    B=[]
    while i<=mid1 and j<=mid2 and k<=last:
        if A[i]<A[j]:
            if A[i]<A[k]:
                B.append(A[i])
                i+=1
            else:
                B.append(A[k])
                k+=1
        else:
            if A[j]>A[k]:
                B.append(A[k])
                k+=1
            else:
                B.append(A[j])
                j+=1
    while i<=mid1 and j<=mid2 and k>last:
        if A[i]<A[j]:
            B.append(A[i])
            i+=1
        else:
            B.append(A[j])
            j+=1
    while i<=mid1 and k<=last and j>mid2:
        if A[i]<A[k]:
            B.append(A[i])
            i+=1
        else:
            B.append(A[k])
            k+=1
    while j<=mid2 and k<=last and i>mid1:
        if A[j]<A[k]:
            B.append(A[j])
            j+=1
        else:
            B.append(A[k])
            k+=1
    while i<=mid1 and j>mid2 and k>last:
        B.append(A[i])
        i+=1
    while j<=mid2 and i>mid1 and k>last:
        B.append(A[j])
        j+=1
    while k<=last and i >mid1 and j>mid2:
        B.append(A[k])
        k+=1
    for i in range(first,last+1):
        A[i]=B[i-first]
        
            
                

def m_sort(A, first, last):
    # 3-way merge sort - merge 함수를 이용해 적절히 합병한다
    if last-first<3:
        C=[]
        if last-first==2:
            for i in range(3):
                C.append(A[first+i])
            C.sort()
            for i in range(first,last+1):
                A[i]=C[i-first]
        elif last-first==1:
            if A[first]>A[last]:
                A[first],A[last]=A[last],A[first]
        return
    mid1=first + (last-first)//3
    mid2=first+2*((last-first)//3)
    m_sort(A,first,mid1)
    m_sort(A,mid1+1,mid2)
    m_sort(A,mid2+1,last)
    merge(A,first,mid1,mid2,last)
    
def check(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return A[0]+A[(len(A)//2)]+A[-1]

A = [int(x) for x in input().split()]
m_sort(A, 0, len(A)-1)
print(check(A))
print(A)