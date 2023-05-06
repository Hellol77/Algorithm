def solution(numbers):
    stack = []
    answer=[0 for i in range(len(numbers))]
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]]<numbers[i]:
            answer[stack.pop()]=numbers[i]
        stack.append(i)
    while stack:
        answer[stack.pop()]=-1
    return answer