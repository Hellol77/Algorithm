function solution(people, limit) {
    people.sort((a,b)=>b-a)
    let answer=0
    let left=0
    let right=people.length-1
    while(left<right){
        if (people[left]+people[right]<=limit){
            left+=1
            right-=1
        }
        else{
            left+=1
        }
        answer+=1
    }
    if (left==right){
        answer+=1
    }
    return answer
}