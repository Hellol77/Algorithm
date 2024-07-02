function solution(arr) {
    const answer=[0,0]
    function recursive(x,y,n){
        let flag=0
        for(let i =x ;i<x+n;i++){
            for (let j =y;j<y+n;j++){
                if (arr[x][y]!==arr[i][j]){
                    flag=1
                    break
                }
            }
        }
        if (flag ==0){
            return answer[arr[x][y]] +=1
        }
        n/=2
        
        recursive(x,y+n,n)
        recursive(x+n,y,n)
        recursive(x,y,n)
        recursive(x+n,y+n,n)
    }
    recursive(0,0,arr.length)
    
    return answer
}