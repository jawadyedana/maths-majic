number = int(input("input number:"))
result = 0
temp = number # creating a copy of a number

while temp != 0:
    digit = temp % 10 # extracting the last digit
    result += digit **3 
    temp = temp // 10 
print(result)
if number == result:
    print(number, "is an armstrong number")
else:
    print(number, "is not an armstrong number")