function solution(edges) {
    const answer =[0,0,0,0]
    function getEdgesMap(){
        const graph = edges.reduce((map,edge)=>{
            if (!map.has(edge[0])){
                map.set(edge[0],[1,0])
            }else{
                const [outside,inside] = map.get(edge[0])
                map.set(edge[0],[1+outside,inside])
            }
            if(!map.has(edge[1])){
                map.set(edge[1],[0,1])
            }else{
                const [outside,inside] = map.get(edge[1])
                map.set(edge[1],[outside,1+inside])
            }
            return map
        },new Map())
        return graph
    }
    const graph= getEdgesMap()
    for (const [key,edge] of graph){
        if (edge[0]>=2 && edge[1]==0){
            answer[0]=key
        }
        else if( edge[0]==0){
            answer[2]+=1
        }
        else if(edge[0]>=2 && edge[1]>=2){
            answer[3]+=1
        }
        
        
    }
    answer[1]=graph.get(answer[0])[0]- answer[2]-answer[3]
    return answer  
}