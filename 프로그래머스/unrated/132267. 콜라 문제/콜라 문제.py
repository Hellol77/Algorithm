def solution(a, b, n):
    count=0
    while n>=a:
        temp=n//a * b
        count+=temp
        rest=n%a
        n=temp+rest
    return count