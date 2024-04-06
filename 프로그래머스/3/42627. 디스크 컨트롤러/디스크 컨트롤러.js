function solution(jobs) {
    const count = jobs.length
    const h = new heap()
    jobs.sort((a,b)=>a[0]-b[0])
    let time=0
    let complete=0
    let total=0
    while(jobs.length||h.size()){
        while(jobs.length){
            if(jobs[0][0]===time){
                h.add(jobs.shift())
            }else break
        }
        if(h.size() && time >=complete){
            const task = h.pop()
            complete = task[1]+time
            total +=complete - task[0]
        }
        time++
        
        
    }
    return total/count>>0
}

class heap{
    constructor(){
        this.heap=[]
        
    }
    
    size(){
        return this.heap.length
        
    }
    
    add(a){
        this.heap.push(a)
        this.bubbleUp()
        
    }
    swap(a,b){
        [this.heap[a],this.heap[b]]=[this.heap[b],this.heap[a]]
    }
    bubbleUp(){
        let index = this.heap.length-1
        let parentIndex = Math.floor((index-1)/2)
        while (this.heap[parentIndex]&& this.heap[parentIndex][1]>this.heap[index][1]){
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
        let leftIndex = index*2+1
        let rightIndex = index*2+2
        while ((this.heap[leftIndex] && this.heap[leftIndex][1] <this.heap[index][1] ) || this.heap[rightIndex] && this.heap[rightIndex][1] < this.heap[index][1]){
            let smallIndex = leftIndex
            if(this.heap[rightIndex]&& this.heap[rightIndex][1]<this.heap[smallIndex][1]){
                smallIndex=rightIndex
            }
            this.swap(smallIndex,index)
            index=smallIndex
            leftIndex = index*2+1
            rightIndex=index*2+2
        }
        
    }
}