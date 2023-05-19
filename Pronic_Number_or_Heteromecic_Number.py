a=int(input())
i=0
j=1
s=0
for i in range(a+1):
    if a==i*j:
        s+=1
        break
    else:
        i+=1
        j+=1
if s!=0:
    print("YES")
else :
    print("NO")
    