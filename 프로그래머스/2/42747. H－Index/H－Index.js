function solution(citations) {
    const length = citations.length
    let answer=0
    citations.sort((a,b)=>b-a)
    citations.forEach((value,index)=>{
        
        if (value >=index+1){
            answer=index+1
        }
        
    })
    return answer
}