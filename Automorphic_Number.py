a=int(input())
b=str(a**2)
if b.endswith(str(a)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")