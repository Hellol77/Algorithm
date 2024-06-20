function solution(files) {
       files.sort((prev, cur) => {
        const regexHead = /^\D+/;
        const regexNumber = /\d{1,5}/;
        
        const prevHead = prev.match(regexHead)[0];
        const curHead = cur.match(regexHead)[0];
         
        const prevNumber = prev.match(regexNumber)[0]
        const curNumber = cur.match(regexNumber)[0]
        
        const compareHead = prevHead.toLowerCase().localeCompare(curHead.toLowerCase())
        
        if (compareHead!==0) return compareHead
        if (prevNumber !== curNumber) return prevNumber- curNumber
       })
    return files
}