function solution(n, k) {
    let numArr = n.toString(k).split("0")
    let answer=0
    for (let i=0;i<numArr.length;i++){
        if (isPrimeNum(numArr[i])){
            answer+=1
        }
    }
    return answer
}
function isPrimeNum (num){
    if (num<=1){
        return false
    }
    for (let i =2 ; i<=Math.sqrt(num);i++){
        if (num %i ==0){
            return false
        }
    }
    return true
    
}