function solution(land) {
    let xx=land.length
    let yy=land[0].length
    let index=2
    let answer=0
    let tempList = [0,0]
    const dfs = (x,y)=>{
        let dxs=[0,0,1,-1]
        let dys=[1,-1,0,0]
        let stack = [[x,y]]
        land[x][y]=index
        let temp=1
        while(stack.length!=0){
            let [tx,ty]=stack.pop()
                for (let i =0 ;i<4;i++){
                    let dx = dxs[i]+tx
                    let dy = dys[i]+ty
                    if (check(dx,dy,land)){
                        temp+=1
                        land[dx][dy]=index
                        stack.push([dx,dy])
                    }
                }
            
        }
        return temp
        
        
    }
    
    let arr=Array.from({length:yy}).fill(0)
    for (let Y =0 ; Y<yy;Y++){
            for (let X=0 ;X<xx;X++){
                if(check(X,Y,land)){
                    let count=dfs(X,Y,land)
                    tempList[index++]=count
                }                
            }
        }
    for (let j =0;j<yy;j++){
        const set = new Set()
        for (let i =0;i<xx;i++){
            set.add(land[i][j])
        }
        let sum = Array.from(set).reduce((a,c)=>a+tempList[c],0)
        if(sum>answer){
            answer=sum
        }
        
    }

return answer
    
    function check (x,y,list){
        if(0<=x && x<xx && 0<=y && y<yy  && land[x][y]==1){
            return true
        }
        else{
            return false
        }
    }
    
}