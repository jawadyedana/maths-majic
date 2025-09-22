def numberofBits(n):
    ones = 0
    zeroes = 0
    while (n):
        if (n & 1 == 1): # condition to check if the last bit is 1 or not
            ones += 1
        else:
            zeroes += 1 
        n >>= 1
    print("number of ones =", ones, "\nNumber of zeroes =", zeroes)

number = int(input("Enter your number: "))
numberofBits(number)