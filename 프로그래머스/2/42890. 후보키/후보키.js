function solution(relation) {
    let combinations = []
    let answer=[]
    let combinationArr=[]
    for(let i =0 ; i <relation[0].length;i++){
        combinationArr.push(i)
    }
    for (let i =1;i<=relation[0].length;i++){
        combinations.push(...getCombination(combinationArr,i))
    }
    combinations.map((combination)=>{
        let s=new Set()
        relation.forEach((r)=>{
            s.add(combination.map((c)=>r[c]).join(''))
        })
        if (relation.length === s.size){
            answer.push(combination)
        }
        
    })
    let results = []
    while (answer.length){
        results.push(answer[0])
        answer = answer.reduce((acc,cur)=>{
            let overlap=answer[0].every(c=>cur.includes(c))
            if(!overlap) acc.push(cur)
            return acc
        },[])
    }
    return results.length
}

function getCombination(arr,selectNum){
    let result=[];
    if(selectNum===1 && arr.length!=0){
        return arr.map(a=>[a])
    }
    arr.forEach((fix,i,origin)=>{
        const rest=origin.slice(i+1);
        const combi=getCombination(rest,selectNum-1);
        const attach=combi.map((c)=>[fix,...c]);
        result.push(...attach)
    })
    return result;
}