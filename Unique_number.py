s=input()
d={}
c=0
for i in s:
    if i in d.keys():
        d[i]+=1
    else :
        d[i]=1
for j in d.values():
    if j!=1:
        c+=1
        break
if c!=1:
    print("Unique Number")
else :
    print("Not Unique Number")