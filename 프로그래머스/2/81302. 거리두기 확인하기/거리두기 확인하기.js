function solution(places) {
    const answer = []
    let dxs=[0,0,1,-1]
    let dys=[1,-1,0,0]

    const dfs =(place,x,y)=>{
        for (let i=0;i<4;i++){
            let dx = dxs[i]+x
            let dy = dys[i]+y
            if(check(dx,dy)){
                if(place[dx][dy]=='P'){
                    return false
                }
                else if (place[dx][dy]==='O'){
                    for (let j=0;j<4;j++){
                        let dxx = dx+dxs[j]
                        let dyy = dy+dys[j]
                        if (check(dxx,dyy)){
                            if(dxx!==x || dyy!==y){
                                if(place[dxx][dyy]==='P'){
                                    return false
                                }
                                
                            }
                        }
                    }
                    
                }
            }
            
        }
        return true
        
    }
    for (const place of places){
        let temp=1
        
    
    for (let i =0 ;i<5;i++){
        for (let j =0;j<5;j++){
            if (place[i][j]=='P'){
                if(!dfs(place,i,j)){
                    temp=0
                    break
                }
            }
                
        }
        if(temp==0){
            break
        }
        
    }
    answer.push(temp)
    }
    return answer
     function check(x,y){
        if(0<=x && x<5 && 0<=y && y<5){
            return true
        }
         return false
        
    }
}
    
  