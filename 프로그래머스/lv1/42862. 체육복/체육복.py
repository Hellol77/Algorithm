def solution(n, lost, reserve):
    setRe = set(reserve)-set(lost)
    setLo = set(lost)-set(reserve)
    for i in setRe:
        if i-1 in setLo:
            setLo.remove(i-1)
        elif i+1 in setLo:
            setLo.remove(i+1)
    return n-len(setLo)