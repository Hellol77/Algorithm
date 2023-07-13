function solution(d, budget) {
    d.sort((a, b) => a - b);
    answer=0
    
    for (var i=0;i<d.length;i++){
        budget-=d[i]
        if (budget<0){
            return answer
            
        }
        answer+=1
    }
    return answer

}