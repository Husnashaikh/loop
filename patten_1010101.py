i=1
a=1
while i<=5:
    n=1
    while n<=a:
        if n%2!=0:
            print("1",end="")
        else:
            print("0",end="")
        n=n+1
    print()
    a=a+2
    i=i+1
