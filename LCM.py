# Input from user
numberlargest = int(input("Enter the first number: "))
numbersmallest = int(input("Enter the second number: "))

# Store original values for LCM formula
a, b = numberlargest, numbersmallest

while numbersmallest:
    numberstore = numbersmallest
    numbersmallest = numberlargest % numbersmallest
    numberlargest = numberstore

gcd = numberlargest
lcm = (a * b) // gcd   # Formula for LCM

print("The GCD is:", gcd)
print("The LCM is:",lcm)
