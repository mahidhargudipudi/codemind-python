s=input()
maxx=0
c=0
for i in s:
    if i in "aeiouAEIOU":
        c+=1
        if c>maxx:
            maxx=c
    else:
        c=0
print(maxx)