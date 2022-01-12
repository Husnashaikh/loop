a=int(input("enter the number"))
i=1
while i<=a:
    j=1
    while j<=a-i:
        print(" ",end="")
        j=j+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
i=1
while a>0:
    b=1
    while b<i:
        print(" ",end="")
        b=b+1
    k=1
    while k<=a:
        print("*",end=" ")
        k=k+1
    print()
    a=a-1
    i=i+1


