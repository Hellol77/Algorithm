function solution(book_time) {
    book_time.sort();
    
    const room=[];
    
    book_time.forEach((t)=>{
        const temp=t[0].split(':');
        
        const start=Number(temp[0])*60 + Number(temp[1])
        
        const idx=room.findIndex((e)=>
            e<=start
        )
        const end = t[1].split(':');
        if (idx===-1){
            
            room.push(Number(end[0])*60+Number(end[1])+10)
        }
        else{
            room[idx]=Number(end[0])*60+Number(end[1])+10
            
        }
        
        
    })
    return room.length
}