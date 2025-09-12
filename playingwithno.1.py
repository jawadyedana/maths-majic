# take input from the user
number = int(input("Enter your number:"))

# store the original number of comparison later
original_number = number
reverse_number = 0

# reverse the number
while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number //= 10

# check if the original number and the new number are the same 
if original_number == reverse_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is  not a palindrome")
