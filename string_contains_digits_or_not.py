def fun(i):
    c=0
    for j in i:
        if j.isdigit():
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")
t=int(input())
for i in range(t):
    s=input()
    fun(s)