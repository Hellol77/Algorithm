function solution(begin, target, words) {
    function check(str1,str2){
        let count=0
        for(let i =0;i<begin.length;i++ ){
            if (str1[i]!==str2[i]){
                count++
            }
        }
        return count===1 ? true :false
        
    }
    
    let q=[]
    let visited = {}
    visited[begin]=0
    q.push(begin)
    while(q.length){
        const now = q.shift()
        
        if(now=== target){
            break
        }
        for (const word of words){
            if(check(now,word) && !visited[word]){
                visited[word]=visited[now]+1
                q.push(word)
            }
        }
        
    }
    return visited[target] || 0
    
}