function solution(arr) {
    function gcd(a,b){
        if (b==0){
            return a
        }
        else if(a%b==0){
            return b 
        }else{
            return gcd(b,a%b)
        }
    }
    let answer=1
    for (let i =0;i<arr.length;i++){
        answer=answer*arr[i]/gcd(answer,arr[i])
    }
    return answer
    
    
    
    
}