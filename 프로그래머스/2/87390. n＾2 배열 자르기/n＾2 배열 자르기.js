function solution(n, left, right) {
    const array=[]
    for (let i =left;i<right+1;i++){
        array.push(Math.max(parseInt(i/n),i%n)+1)
    }
    return array
}