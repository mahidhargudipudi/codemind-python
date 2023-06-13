maxx=0
c=0
s=input()
st=s.lower()
for i in st:
    if i in "aeiou":
        c+=1
        if c>maxx:
            maxx=c
    else:
        c=0
print(maxx)