function solution(dice) {
    const combination = []
    const temp=[]
    let n = dice.length
    let answer=[]
    let max=0
    const array =new Array(n).fill(0).map((a,i)=>i)
    const dfs=(N,prev=0)=>{
        if(temp.length ===N/2){
            combination.push([...temp])
            return
        }
        for (let i =prev;i<N ;i++){
            temp.push(i)
            dfs(N,i+1)
            temp.pop()
        }
    }
    
    dfs(n)
    
    combination.forEach(dice1=>{
        const dice2 = array.filter((a)=>!dice1.includes(a) )
        console.log(dice1)
        console.log(dice2)
        const sum1 = getSumList(dice,dice1)
        const sum2 = getSumList(dice,dice2).sort((a,b)=>a-b)
        let count=0
        
        for(let i =0;i<sum1.length;i++){
            count+=getVictoryCount(sum1[i],sum2)
        }
        if(count>max){
            max=count
            answer=dice1
        }
         
        
        
        
    })
    return answer.map((a)=>a+1)
    
     
}
  function getComb(L,array){
    if(L ===1){
        return array.map(a=>[a])
    }
    const result=[]
    for(let i=0;i<array.length;i++){
        const rest = array.slice(i+1)
        const comb = getComb(L-1,rest)
        const attach = comb.map(c=>[array[i],...c])
        result.push(...attach)
    }
    return result
}
const getVictoryCount = (n,list)=>{
        let left =0
        let right=list.length-1
        

        if(n>list[right]){
            return right+1
        }
        while(left<right){
        let mid = Math.floor((left+right)/2)
            
    
        if(n>list[mid]){
            left=mid+1
        }else{
            right=mid
        }
    }
        return right
    }
                        
function getSumList (dice, list){
   let tmp = [...dice[list[0]]]
   for(let i=1;i<list.length;i++){
       const tmp1 =[]
       for(let j=0;j<tmp.length;j++){
           for(let k=0;k<6;k++){
               tmp1.push(dice[list[i]][k]+ tmp[j])
           }
       }
       tmp = tmp1
   }
    return tmp
}
