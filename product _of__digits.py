num=int(input("enter the number"))
rem=0
sum=1
while num>0:
    rem=num%10
    sum=sum*rem
    num=num//10
print(sum)
