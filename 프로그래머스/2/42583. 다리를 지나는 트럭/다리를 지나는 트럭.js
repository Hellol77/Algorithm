function solution(bridge_length, weight, truck_weights) {
    let time = 0
    const crossing = new Array(bridge_length).fill(0)
    let crossingSum = 0
    
    
    crossing.shift()
    crossingSum +=truck_weights[0]
    crossing.push(truck_weights.shift())
    time++
    while (crossingSum>0){
        time++
        
        crossingSum -=crossing.shift()
        
        if (truck_weights.length>0 && crossingSum+truck_weights[0]<=weight){
            crossingSum +=truck_weights[0]
            crossing.push(truck_weights.shift())
        }else{
          crossing.push(0);
        }
    }
    return time
}