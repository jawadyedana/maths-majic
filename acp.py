#one
T(n) = O(n) + T(n/2) + T(n/3)

# two
def myfunction2(n):
 if (n<=1):
    return 
 print("Codingal")
 myfunction2(n-1)

 T(n) = O(1) + T(n-1)