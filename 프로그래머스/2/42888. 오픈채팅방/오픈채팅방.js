function solution(record) {
    const nameMap = new Map()
    const temp=record.map((v)=>v.split(' '))
    
    temp.forEach((v)=>{
        if(v[0]==='Enter' || v[0]==='Change'){
            nameMap.set(v[1],v[2])
            
        }
        
    })
    const answer=[]
    temp.forEach((v)=>{
        if(v[0]==='Enter'){
            answer.push(`${nameMap.get(v[1])}님이 들어왔습니다.`)
        }
        if(v[0]==='Leave'){
            answer.push(`${nameMap.get(v[1])}님이 나갔습니다.`)
        }
        
    })
    return answer
    
}