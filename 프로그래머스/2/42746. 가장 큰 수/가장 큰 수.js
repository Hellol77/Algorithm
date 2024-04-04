function solution(numbers) {
    const arr = numbers.map(number =>String(number))
    const answer=arr.sort((a,b)=>(b+a)-(a+b)).join('')
    
    return answer[0] ==='0' ? '0': answer
}