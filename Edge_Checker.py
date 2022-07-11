a,b=map(int,input().split())
if b>a:
    a,b=b,a
if a-b==1 or a-b==9:
    print("Yes")
else:
    print("No")