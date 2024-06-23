function solution(sequence) {
    const dp = new Array(sequence.length).fill(0).map(()=>new Array(2).fill(0))
    let plusOperator = -1
    const plus = sequence.map((value)=>{
        plusOperator*=-1
        return value*plusOperator
        
    })
    let minusOperator = 1
    const minus= sequence.map((value)=>{
        minusOperator*=-1
        return value*minusOperator
    })
    
    dp[0][0]=plus[0]
    dp[0][1]=minus[0]
    answer1=plus[0]
    answer2=minus[0]
    for (let i =1;i<dp.length;i++){
        dp[i][0]=Math.max(dp[i-1][0]+plus[i],plus[i])
        dp[i][1]=Math.max(dp[i-1][1]+minus[i],minus[i])
        
        answer1=Math.max(answer1,dp[i][0])
        answer2=Math.max(answer2,dp[i][1])
    }
    
    return Math.max(answer1,answer2)
}
