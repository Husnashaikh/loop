a=1
while a<=100:
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count=count+1
        i=i+1
    if count==2:
        print(a)
    a=a+1
