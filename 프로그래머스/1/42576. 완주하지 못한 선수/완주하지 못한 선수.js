function solution(participant, completion) {
    const m = new Map()
    let answer=''
    participant.map((key)=>{
        if (m.has(key)){
            m.set(key,m.get(key)+1)
        }
        else{
            m.set(key,1)
        }
    })
    completion.map((key)=>{
            m.set(key,m.get(key)-1)
    })
    m.forEach((value,key)=>{
        if (value!=0){
            answer=key
        }
        
    })
    return answer
}