function solution(n, computers) {
    let answer=0
    let visited = []
    function dfs(index){
        
        visited.push(index)
        for (let i=0;i<n;i++){
            if(computers[index][i]==1 && visited.includes(i)==false){
                dfs(i)
            }
            
        }
        
        
    }
    
    for (let i =0 ; i<n; i++){
        if(visited.includes(i)==false){
            dfs(i)
            answer++
        }
        
    }
    return answer
}