function solution(n, wires) {
    let answer=Number.MAX_SAFE_INTEGER; 
    const graph=Array.from({length:n+1} ,()=>[])
    wires.forEach((v)=>{
        graph[v[0]].push(v[1])
        graph[v[1]].push(v[0])
    })
    function bfs(start,except){
        let q=[start]
        let count = 0
        let visited= Array.from({length:n+1},()=>false)
        visited[start]=true
        
        while(q.length){
            let index=q.shift()
            graph[index].forEach((element)=>{
                if(element !==except && visited[element]==false  ){
                    q.push(element)
                    visited[element]=true
                }
            })
            count++
        }
        
        return count
    }
    wires.forEach((element)=>{
        let [start,end]=element
        answer = Math.min(answer,Math.abs(bfs(start,end) - bfs(end,start)))
        
    })
    return answer
}