def Greatest(a,b,c):

    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))

    if(a>b and a>c):
        print("a is greatestnumber:",a)
    elif(b>a and b>c):
        print("b is greatest number :",b)
    else:
        print("c is greatest number :",c)
Greatest(1 ,2 ,3)