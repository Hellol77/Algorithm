function solution(rectangle, characterX, characterY, itemX, itemY) {
    characterX *=2
    characterY *=2
    itemX*=2
    itemY*=2
    
    let doubleArr = rectangle.map(rec => rec.map(point=>point * 2))
    const dxs= [1,-1,0,0]
    const dys = [0,0,1,-1]
    
    const start = [characterX,characterY,0]
    let q=[start]
    let arr = Array.from({length:103},()=>Array(103).fill(0))
    doubleArr.forEach(([x1,y1,x2,y2])=>{
        for (let i =x1;i<=x2 ;i++){
            for (let j =y1 ;j<=y2 ;j++){
                if(i===x1||i===x2||j===y1||j===y2){
                    if(arr[i][j]===0) arr[i][j]=1;
                }else{
                    arr[i][j]=2
                }
                
            }
            
        }
        
        
    })
    
    arr[characterX][characterY]=0
    
    while(q.length>0){
        let [x,y,c]=q.shift()
        
        if(x===itemX && y===itemY) return c/2
        
        for (let i =0 ; i<4;i++){
            let dx = dxs[i]+x
            let dy = dys[i]+y
            if(arr[dx][dy]===1){
                q.push([dx,dy,c+1])
                arr[dx][dy]=0
            }
            
        }
        
    }
    return 0
}