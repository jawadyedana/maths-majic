def power4(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0 and (number - 1) % 3 == 0

n = int(input("enter a number:"))
if power4(n):
    print("\n the number is a power of 4")
else:
    print("\n the number is not a power of 4")