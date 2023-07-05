function solution(n) {
    arr=[n]
    for(var i=1;i<=n/2;i++){
        if(n%i==0){
            arr.push(i)
            
            
       }
        
        
    }
    var answer=0
    for (var i=0;i<arr.length;i++){
        answer+=arr[i]
        
    }
    return answer
}