def checkRightmostSetBit(number):
    if number == 0:
        print("No bits are set.")
    else:
        rightmost_set_bit = number & -number
        print(f"Rightmost set bit is: {rightmost_set_bit}")
        print(f"Position of rightmost set bit (0-indexed from right): {rightmost_set_bit.bit_length() - 1}")

number = int(input("enter the number: "))
checkRightmostSetBit(number)