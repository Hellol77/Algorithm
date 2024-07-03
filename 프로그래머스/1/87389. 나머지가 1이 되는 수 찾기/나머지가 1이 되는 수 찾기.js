function solution(n) {
    let nn=n-1
    for (let i =2 ; i<=nn;i++){
        if (nn%i==0){
            return i
        }
    }
    
}