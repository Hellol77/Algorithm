function solution(scoville, K) {
    const arr=new heap()
    let answer=0
    scoville.map((value)=>{
        arr.add(value)
        
    })
    while (arr.size()>1 && arr.peek()<K){
        const one = arr.pop()
        const two = arr.pop()
        const mix = one + (two*2)
        arr.add(mix)
        answer++
    }
    
    return arr.peek() >=K ? answer : -1 
}

class heap {
    constructor(){
        this.heap=[]
        
    }
    peek(){
        return this.heap[0]
    }
    size(){
        
        return this.heap.length
    }
    
    swap(idx1, idx2){
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
    }
    
    add(value){
        this.heap.push(value)
        this.bubbleUp()
        
    }
    bubbleUp(){
        let index = this.heap.length -1
        let parentIndex = Math.floor((index-1)/2)
        while(this.heap[parentIndex] && this.heap[index] < this.heap[parentIndex]){
            this.swap(index,parentIndex)
            index=parentIndex
            parentIndex=Math.floor((index-1)/2)
            
        }
        
    }
    
    pop(){
        if(this.heap.length===1){
            return this.heap.pop()
        } 
        const value = this.heap[0]
        this.heap[0]=this.heap.pop()
        this.bubbleDown()
        return value
    }
    
    bubbleDown(){
        let index=0
        let leftIndex = index * 2 + 1
        let rightIndex = index * 2 + 2
        while ((this.heap[leftIndex] && this.heap[index]>this.heap[leftIndex]) || this.heap[rightIndex]&& this.heap[index] >this.heap[rightIndex]){
            let smallIndex = leftIndex
            if(this.heap[rightIndex] && this.heap[rightIndex] <this.heap[smallIndex]){
                smallIndex=rightIndex
            }
            this.swap(smallIndex,index)
            index=smallIndex
            leftIndex = index*2+1
            rightIndex= index*2+2
            
        }
        
    }
    
    
}