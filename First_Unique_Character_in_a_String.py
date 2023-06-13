a=input().strip()
l=[]
for i in a :
    if i not in l and a.count(i)==1:
        l.append(i)
if len(l)==0:
    print("-1")
else:
    ind=a.index(l[0])
    print(ind)