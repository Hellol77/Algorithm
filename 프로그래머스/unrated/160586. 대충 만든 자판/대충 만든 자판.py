def solution(keymap, targets):
    answer=[]
    for i in targets:
        times=0
        for char in i:
            flag=-1
            time=101
            for key in keymap:
                if char in key:
                    time=min(key.index(char)+1,time)
                    flag=1
            if flag==-1:
                times=-1
                break
            times+=time
        answer.append(times)
    return answer
            
                    