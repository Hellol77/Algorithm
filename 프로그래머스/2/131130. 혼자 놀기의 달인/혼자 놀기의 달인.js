function solution(cards) {
    let answer=[]
    cards.forEach((value,i)=>{
        let index=i
        let count=0
        
        while(true){
            if(cards[index]){
                let temp = cards[index]
                cards[index]=0
                index=temp-1
                count++
            }
            else{
                if(count==0){
                    break
                }
                answer.push(count)
                break
            }
        }
        
    })
    const sortAnswer = answer.sort((a,b)=>b-a)
    return sortAnswer.length >1 ?sortAnswer[0]*sortAnswer[1] : 0
}