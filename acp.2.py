def binary_to_decimal(binary):
    decimal = 0
    for i, bit in enumerate(binary[::-1]):
        decimal += int(bit) * 2 ** i
    return decimal

# Example usage:
binary = input("Enter a binary number: ")
try:
    decimal = binary_to_decimal(binary)
    print(f"The decimal equivalent of {binary} is: {decimal}")
except ValueError:
    print("Invalid binary number. Please enter only 0s and 1s.")