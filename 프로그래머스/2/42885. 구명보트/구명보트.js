function solution(people, limit) {
    people.sort((a,b)=>b-a)
    console.log(people)
    let answer=0
    let box = 100
    while(people.length !==0){
            if (box>=people[people.length-1]){
                box -=people[people.length-1]
                people.pop()
                if (people.length==0){
                    answer+=1
                    break
                }
            }
            else if (box<people[people.length-1]){
                answer+=1
                box=100
            }
        }
    return answer
}