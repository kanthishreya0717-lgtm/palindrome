import sys
string = sys.argv[1] if len(sys.argv) > 1 else "madam"

if string == string[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")