a=input()
count =0
temp='3'
for i in a:
    if i!=temp:
        temp=i
        count+=1
        
print(count//2)