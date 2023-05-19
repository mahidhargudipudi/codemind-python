def fact(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s=s+i
    return s
a=int(input())
b=int(input())
if fact(a)==fact(b):
    print("Amicable")
else :
    print("Not Amicable")