i=1
while i<6:
    number=int(input("enter the number"))
    if number<5:
        print("smaller")
    elif number==5:
        print("wow you guess the correct number")
    else:
        print("greater")
        break
    i=i+1
    print(i)