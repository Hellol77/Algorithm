import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())

arr = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(n):
    numbers, s, b = map(int, sys.stdin.readline().split())
    numbers = list(map(int, str(numbers)))

    new_arr = []

    for num in arr:
        strike = 0
        ball = 0

        for i in range(3):
            if num[i] == numbers[i]:
                strike += 1
            elif num[i] in numbers:
                ball += 1

        if strike == s and ball == b:
            new_arr.append(num)

    arr = new_arr

# 가능한 숫자의 개수를 출력합니다.
print(len(arr))
