def numberofBits(n):
    ones = 0
    zeroes = 0
    max_consecutive_ones = 0
    current_consecutive_ones = 0
    
    while (n):
        if (n & 1 == 1): 
            ones += 1
            current_consecutive_ones += 1
            max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
        else:
            zeroes += 1
            current_consecutive_ones = 0
        n >>= 1
    
    print("Number of ones =", ones, "\nNumber of zeroes =", zeroes)
    print("Longest consecutive 1s =", max_consecutive_ones)

number = int(input("Enter your number: "))
numberofBits(number)
