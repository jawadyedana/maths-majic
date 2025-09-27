def power2(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0

n = int(input("enter a number:"))
if power2(n):
    print("\n the number is a power of 2")
else:
    print("\n the number is not a power of 2")