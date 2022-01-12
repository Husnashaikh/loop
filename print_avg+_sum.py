sum=0
avg=1
i=1
while i<=5:
    num=int(input("enter the number"))
    sum=sum+num
    avg=num/5
    i=i+1
print("sum",sum)
print("avg",avg)
if avg%5==0:
    print("itis divisible by 5")
else:
    print("not")