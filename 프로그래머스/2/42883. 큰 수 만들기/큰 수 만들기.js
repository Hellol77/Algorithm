function solution(number, k) {
    const arr=[]
    for(let i =0 ; i<number.length;i++){
        while (arr.length>0 && arr[arr.length-1]<number[i] && k>0){
            arr.pop()
            k--
        }
        arr.push(number[i])
    }
    arr.splice(arr.length-k,k)
    return arr.join('')
}