function solution(n, words) {
    let s = new Set()
    let indexCount = 0
    let count = 1
    let tempCount=1  
    s.add(words[0])
    let word = words[0]
    for(let i =1 ; i<words.length;i++){
        if (word[word.length-1]!==words[i][0] || s.has(words[i])){
            indexCount = i % n +1
            tempCount = Math.floor(i/n) +1
            return [indexCount,tempCount]
            
        }
        s.add(words[i])
        word = words[i]
        
    }
    return [0,0]
}