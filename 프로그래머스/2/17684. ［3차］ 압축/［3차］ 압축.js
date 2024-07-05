function solution(msg) {
    const answer=[]
    const arr=Array(26).fill().map((v, i) => String.fromCharCode(i + 65));
    let lastcount = 27
    let nextWord = ""
    const dic = arr.reduce((d,a,index)=>{
      return (d[a]=index+1,d)
    },{})
    
    const s= msg.split("").reduce((acc,cur)=>{
        nextWord = acc+cur
        if (dic[nextWord]===undefined){
            dic[nextWord]=lastcount++
        }else{
            return acc+cur
        }
        
        if(dic[acc]!==undefined) answer.push(dic[acc])
        return cur
        
    })
    
    answer.push(dic[s])
    return answer
        
}