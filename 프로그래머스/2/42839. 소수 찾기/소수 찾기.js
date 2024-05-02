function solution(numbers) {
    
    const arr=numbers.split('')
    const s=new Set()
    function solve(array,fixed){
        if(array.length>0){
            for(let i =0 ;i<array.length;i++){
                let newFixed = fixed+array[i]
                let copyArray = [...array]
                copyArray.splice(i,1)
                if(isPrime(parseInt(newFixed))){
                    s.add(parseInt(newFixed))
                }
                solve(copyArray,newFixed)
            }
        }
    }
    solve(numbers,"")
    return s.size
    
    
    function isPrime(num){
        if(num<2){
            return false
        }
        for (let i =2;i<num;i++){
            if(num%i==0){
                return false
            }
        }
        return true
    }
}