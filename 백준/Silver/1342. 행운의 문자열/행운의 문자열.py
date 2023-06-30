from sys import stdin
input = stdin.readline

def dfs(depth, string):
    global N, cnt

    if depth == N:
        cnt += 1
        return
    for char in charSet:
        idx = ord(char) - 97
        if charCnt[idx] == 0:
            continue
        if string and string[-1] == char:
            continue
        charCnt[idx] -= 1
        dfs(depth + 1, string + char)
        charCnt[idx] += 1


String = input().strip()
charCnt = [0] * 26
N = len(String)
cnt = 0
charSet = set()

for char in String:
    idx = ord(char) - 97
    charCnt[idx] = charCnt[idx] + 1
    charSet.add(char)

dfs(0, '')
print(cnt)