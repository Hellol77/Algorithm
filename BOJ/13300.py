n,k=map(int,input().split())
arr=[[0,0] for i in range(7)]
room=0
for i in range(n):
    gender,grade=map(int,input().split())
    arr[grade][gender]+=1

for a,b in arr:
    room+=a//k
    room+=b//k
    if a%k:
        room+=1
    if b%k:
        room+=1
print(room)
        