from collections import defaultdict

def part(s):
    arr = []
    for i in range(len(s) - 1):
        p = s[i:i + 2]
        if not p[0].isalpha() or not p[1].isalpha():
            continue
        arr.append(p.lower())
    return arr


def solution(str1, str2):
    part1 = part(str1)
    part2 = part(str2)
    
    # 둘 다 비어있을 경우
    if not part1 and not part2:
        return 65536

    # 두 문자열의 다중집합 표현
    s1 = defaultdict(int)
    s2 = defaultdict(int)
    for i in part1:
        s1[i] += 1
    for i in part2:
        s2[i] += 1

    # 합집합과 교집합 계산
    u = 0  # 합집합 크기
    n = 0  # 교집합 크기

    # s1 기준으로 계산
    for key in s1:
        if key in s2:
            n += min(s1[key], s2[key])  # 교집합 크기
            u += max(s1[key], s2[key])  # 합집합 크기
        else:
            u += s1[key]  # 합집합에만 포함

    # s2에만 있는 값 추가
    for key in s2:
        if key not in s1:
            u += s2[key]  # 합집합에만 포함

    # 자카드 유사도 계산
    return int((n / u) * 65536)
