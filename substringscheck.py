def allSubstrings(s):
    substrings = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    return substrings

string = input("Enter your string: ")
substrings = allSubstrings(string)
print("All substrings:")
print(substrings)