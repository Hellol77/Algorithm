answer=0
idx=-1
def solution(word):
    dxs = ['A', 'E', 'I', 'O', 'U']
    def dfs(count,w):
        global answer, idx
        if len(w)<=5:
            idx+=1
            if w==word:
                print(w)
                answer=idx
        else:
            return
        for i in range(5):
            dfs(count+1,w+dxs[i])
            
    dfs(0,'')
    return answer
    
        