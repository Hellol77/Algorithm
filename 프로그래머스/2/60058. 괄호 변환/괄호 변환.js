function solution(p) {
    const stack = []
    if (p==""){
        return ""
    }
    const {u,v} = uv(p)
    if (checkCorrect(u)){
        
        const temp=solution(v)
        return u+temp
        
    }
    else{
        let newU=""
        if (u.length <=2){
            newU=""
        }else{
            for (let string of u.slice(1,-1)){
                if (string =='('){
                    newU+=')'
                
                }
                else{
                    newU+='('
                }
            }
        }
        let newString = "("+ solution(v) +")" +newU
        return newString   
    }
}

function checkCorrect(p){
    let stack = []
    
    for (let string of p){
        if (string=='('){
            stack.push(string)
        }
        else{
            if(stack.length!==0 && stack[stack.length-1]=='('){
                stack.pop()
            }else{
                return false
            }
            
        }
    }
    if (stack.length === 0){
        return true
    }
    return false
}

function uv (p){
    let left = 0
    let right =0
    let u =''
    let v =''
    for (let string of p){
        
        if (left!==right ||( left==0 && right==0)){
            if (string=='('){
                u+=string
                left+=1
            }
            else if (string==')'){
                u+=string
                right+=1
            }
        }
        else if (left==right){
            v+=string
        }
    }
    return {u,v}
}