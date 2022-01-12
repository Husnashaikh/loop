s=input("enter the word :")
count=0
con=0
i=0
while i<len(s):
    if (s[i]=="a" or s[i]=="i" or s[i]=="u" or s[i]=="e" or s[i]=="o"):
        count+=1
        print(s[i],"vowel")
    else:
        con+=1
        print(s[i],"consonant")
    i+=1
print("vowel",count)
print("Cons",con)    