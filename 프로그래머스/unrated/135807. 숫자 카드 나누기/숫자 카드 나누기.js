const gcd = (n1, n2) => {
  let remainder = n1 % n2;
  return n2 === 0 ? n1 : gcd(n2, remainder);
};

function solution(arrayA, arrayB) {
    let answer=0
    let [gcdA ,gcdB]=[arrayA[0],arrayB[0]]
    for (let i =1;i<arrayA.length;i++){
        gcdA=gcd(arrayA[i],gcdA)
        gcdB=gcd(arrayB[i],gcdB)
        
    }
    if (gcdA ===1) gcdA=0
    if (gcdB ===1) gcdB=0
    
   if (arrayA.every((i)=>i%gcdB!==0))answer=Math.max(answer,gcdB);
    if (arrayB.every((i)=>i%gcdA!==0))answer=Math.max(answer,gcdA);
    
    return answer;
    
}