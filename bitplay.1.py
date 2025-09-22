def setOrNot(number, n):
    if number & (n<< (n - 1)):
        print("SET")
    else:
        print("NOT SET")
number = int(input("enter the number: "))
n = int(input("enter the bit position: "))
setOrNot(number, n)
                     