s=input()
c=0
for i in s:
    if i.isdigit():
        c+=1
if c>0:
    print("Contains {} digit".format(c))
else:
    print("Doesn't contain digit")