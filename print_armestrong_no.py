a=int(input("enter the number"))
num=a
sum=0
while (a>0):
    sum=sum+(a%10)*(a%10)*(a%10)
    a=a//10
if num==sum:
    print("it is armstrong number")
else:
    print("it is not a armstrong number")
