function solution (begin, end) {
const answer=[]  
  for(let i = begin; i <= end; i++) {
    answer.push(getMaxDivisor(i))
  }
    
  return answer;
}

const getMaxDivisor = (n) => {
    const check=[]
    if (n==1){
        return 0
    }
    
  for(let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      check.push(i)
        if (n/i<=1e7){
            return n/i
        }
    }
  }
    if(check.length!==0){
        return check[check.length-1]
    }
  return 1;
}