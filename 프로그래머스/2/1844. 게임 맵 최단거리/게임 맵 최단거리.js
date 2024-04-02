function solution(maps) {
    
    let goal = {x:maps.length -1,y:maps[0].length -1}
    let q=[]
    let dxs=[0,0,1,-1]
    let dys=[1,-1,0,0]
    q.push([0,0,1])
    while (q.length){
        const [x,y,move]=q.shift()
        if (x==goal.x && y==goal.y){
            return move
        }
        for (let i=0 ; i<4;i++){
                let dx=dxs[i]+x
                let dy=dys[i]+y
                if (check(dx,dy)){
                    q.push([dx,dy,move+1])
                    maps[dx][dy]=0                   
                }
            }
        
        }
    return -1
    
function check(x,y){
    if (0<=x && x<maps.length && 0<=y && y<maps[0].length  && maps[x][y]==1){
        return true
    }
    return false
    
}    
    

}
    
    
