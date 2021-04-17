def Palindrome():
    num=int(input("enter the number "))
    temp=num
    pal=0
    while(num>0):
        dig=num%10
        pal=pal*10+dig
        num=num//10
    if(temp==pal):
        print("its a Palindrome number")
    else:
        print("its not a Palindrome number")
    
Palindrome()
