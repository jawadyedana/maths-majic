def reverseBits(number):
    result = 0
    for _ in range(32):  # Considering 32-bit integer
        result = (result << 1) | (number & 1)
        number >>= 1
    print(f"Number after reversing bits: {result}")

number = int(input("enter the number: "))
reverseBits(number)