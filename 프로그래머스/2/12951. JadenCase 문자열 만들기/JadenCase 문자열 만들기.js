function solution(s) {
    const arr = s.split(" ")
    
    const answer=arr.map((v)=>{
        return v.substr(0,1).toUpperCase()+v.substr(1).toLowerCase()
        
    })
    return answer.join(" ")
}