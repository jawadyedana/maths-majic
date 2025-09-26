def TwoOdd(arr, size):
    xor = 0
    x = 0
    y = 0
    setBit = 0

    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]
    setBit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if(arr[i]& setBit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    
    print("TwoOdd elements are",x, "&", y)

arr = []
arr_size= int(input("enter the array size:"))
for i in range(0, arr_size):
    z = int(input("enter the element:"))
    
    arr.append(z)

TwoOdd(arr, arr_size)