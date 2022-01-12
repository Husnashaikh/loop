i=int(input("enter the number"))
x=i
rev=0
while (i>0):
    rev=rev*10+i%10
    i=i//10
if (x==rev):
    print(x,"is a palindorme number")
else:
    print(x,"not a palindorme number")