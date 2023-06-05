n=int(input())
ls=list(map(int,input().split()))
l=[]
d={}
for i in ls:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for k in d.values():
    if k>1:
       l.append(k//2)
print(sum(l)) 