function solution(land) {
    const dp = new Array(land.length).fill(0).map(()=>new Array(land[0].length).fill(0))
    const rowLength = land.length
    const columnLength = land[0].length
    for (let i =0;i<columnLength;i++){
        dp[0][i] = land[0][i]
    }
    for (let i =1;i<rowLength;i++){
        for (let j=0;j<columnLength;j++){
            dp[i][j]=Math.max(...dp[i-1].filter((v,index)=>{
                return index!==j
            }))+land[i][j]
        }
    }
    return Math.max(...dp[rowLength-1])
}