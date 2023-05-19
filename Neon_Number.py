a=int(input())
s=a**2
su=0
while s:
    rem=s%10
    su=su+rem
    s=s//10
if a==su:
    print("Neon Number")
else:
    print("Not Neon Number")