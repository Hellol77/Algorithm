def solution(dirs):
    location = [0,0]
    answer=[]
    
    for i in dirs:
        if i=='U' and location[1]!=5:
            move = [location[0],location[1]+1]
            temp = [location,move]
            temp2 = [move,location]
            if temp not in answer and temp2 not in answer:
                answer.append(temp)
                answer.append(temp2)
            location=move

        elif i=='D' and location[1]!=-5:
            move = [location[0],location[1]-1]
            temp = [location,move]
            temp2 = [move,location]
            if temp not in answer and temp2 not in answer:
                answer.append(temp)
                answer.append(temp2)
            location=move

        elif i =='R' and location[0]!=5:
            move = [location[0]+1,location[1]]
            temp = [location,move]
            temp2 = [move,location]
            if temp not in answer and temp2 not in answer:
                answer.append(temp)
                answer.append(temp2)
            location=move

        elif i=='L' and location[0]!=-5:
            move = [location[0]-1,location[1]]
            temp = [location,move]
            temp2 = [move,location]
            if temp not in answer and temp2 not in answer:
                answer.append(temp)
                answer.append(temp2)
            location=move
    return len(answer)//2
    