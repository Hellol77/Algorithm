def solution(video_len, pos, op_start, op_end, commands):
    def calTime (stringTime):
        arr=list(stringTime.split(":"))
        
        return int(arr[0])*60 + int(arr[1])
    
    currentTime = calTime(pos)
    finishTime = calTime(video_len)
    opStart = calTime(op_start)
    opEnd = calTime(op_end)
    
    def calStringTime(numberTime):
        hour = numberTime//60
        minute = numberTime%60
        if hour<10:
            hour = '0'+str(hour)
        if minute <10:
            minute = '0'+str(minute)
        return str(hour)+":"+str(minute)
    
    for i in commands:
        if opStart<=currentTime <= opEnd:
            currentTime = opEnd
        if i=="next":
            currentTime +=10
            if finishTime<currentTime:
                currentTime=finishTime
        elif i=="prev":
            currentTime -= 10
            if 0>currentTime:
                currentTime=0
        if opStart<=currentTime <= opEnd:
            currentTime = opEnd
            
    return calStringTime(currentTime)
            