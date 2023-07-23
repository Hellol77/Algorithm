function solution(k, tangerine) {
    const obj={}
    
    tangerine.forEach((i)=>{
        obj[i]=++obj[i]||1
        
        
    })
    let count=0
    let answer=0
    const sortObj = Object.values(obj).sort((a,b)=>b-a) //내림차순
    for (let num of sortObj){
        answer++;
        count+=num;
        if(k<=count){
            break
            
        }
    }
    return answer
}