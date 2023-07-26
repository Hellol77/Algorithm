function solution(k, ranges) {
    let x=0
    let endx=0
    const arr=[]
    const answer=[]
    while(k!=1){
        arr.push([x++,k])
        
        if(k%2!==0){
            k=k*3+1
            
        }
        else{
            k/=2
        }
        
    }
    if(k===1){
        arr.push([x,k])
        endx=x
    }
    for(let i of ranges){
        let vx = i[0]
        let ex=endx+i[1]
        let result = 0
        if (vx>ex){
            answer.push(-1)
            continue;
        }
        for (let j=vx;j<ex;j++ ){
            result+=1*(arr[j][1]+arr[j+1][1])/2
            
            
        }
        answer.push(result)

        
    }
    return answer
}