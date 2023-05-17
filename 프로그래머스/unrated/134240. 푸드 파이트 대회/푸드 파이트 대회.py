def solution(food):
    answer = '0' # 정답 가운데에는 항상 '0'
    for i in range(len(food)-1,0,-1): # 칼로리가 큰 음식부터 음식의 번호(문자열)를 (음식의 양/2)번만큼 문자열 오른쪽과 왼쪽에 추가
        answer=str(i)*(food[i]//2)+answer
        answer=answer+str(i)*(food[i]//2)
    return answer