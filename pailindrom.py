# Palindrome
# A string is a palindrome when it is the same when read backwards.
# For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a
#  palindrome, because "abcd" != "dcba".
# Write a function named palindrome that takes a single string as its parameter. Your function
#  should return True if the string is a palindrome, and False otherwise.


def palindrome(chr):
    i=0
    j=0
    while i<len(chr):
        j=chr[-1::-1]
        i=i+1
    if (chr==j):
        return "palindrome"
    else:
        return "not a palindrome"
print(palindrome(chr=input("enter your charecter: ")))
