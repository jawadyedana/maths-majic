def CheckIfState(number1,number2):
    if(number1^number2)!=0:
        print("numbers are not equal")
              
    else:
         print("both numbers are equal")

number1=int(input("enter first number to compare"))

number2=int(input("enter fsecond number to compare"))

CheckIfState(number1,number2)

