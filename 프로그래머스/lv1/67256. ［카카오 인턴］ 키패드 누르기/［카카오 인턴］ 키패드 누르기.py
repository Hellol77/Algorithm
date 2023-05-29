def solution(numbers, hand):
    answer=''
    pos = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],'*':[3,0],0:[3,1],'#':[3,2]}
    leftHand=pos['*']
    rightHand=pos['#']
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            leftHand=pos[i]
        elif i in [3,6,9]:
            answer+='R'
            rightHand=pos[i]
        else:
            if abs(leftHand[0]-pos[i][0])+abs(leftHand[1]-pos[i][1])>abs(rightHand[0]-pos[i][0])+abs(rightHand[1]-pos[i][1]):
                rightHand=pos[i]
                answer+='R'
            elif abs(leftHand[0]-pos[i][0])+abs(leftHand[1]-pos[i][1])<abs(rightHand[0]-pos[i][0])+abs(rightHand[1]-pos[i][1]):
                leftHand=pos[i]
                answer+='L'
            else:
                if hand=='right':
                    rightHand=pos[i]
                    answer+='R'
                else:
                    leftHand=pos[i]
                    answer+='L'
                    
    return answer
        
        
    
                   
        
            