def solution(N, stages):
    result={}
    participate=len(stages)
    for i in range(1,N+1):
        if participate!=0:
            count=stages.count(i)
            result[i]=count/participate
            participate-=count
        else:
            result[i]=0
    return sorted(result,key=lambda x : result[x],reverse=True)
