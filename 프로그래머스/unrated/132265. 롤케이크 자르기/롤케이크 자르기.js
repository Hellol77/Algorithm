function solution(topping) {
    
    let answer=0
    let map1 = new Map()
    let map2 = new Map()
    topping.forEach((n)=>{
        map1.set(n,(map1.get(n) || 0) + 1)
        
    })
    
    for (let i of topping){
        
        map1.set(i,map1.get(i)-1)  
        map2.set(i,true)
        if( !map1.get(i)){
            map1.delete(i)     
        }
        if (map1.size===map2.size){
            
            answer+=1
        }
        if (map1.size<map2.size){
            
            break
        }
        
        
    }
    return answer
  

} 