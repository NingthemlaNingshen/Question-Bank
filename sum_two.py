# Return the Sum of Two Numbers
# Create a function that takes two numbers as arguments and returns their sum.
# Examples
# addition(3, 2) ➞ 5
 
# addition(-3, -6) ➞ -9
 
# addition(7, 3) ➞ 10
# Notes
# Don't forget to return the result.
# If you get stuck on a challenge, find help in the Resources tab.
# If you're really stuck, unlock solutions in the Solutions tab.


def sum_of_two(a):
    i=0
    s=0
    while i<len(a):
        s=s+a[i]
        i=i+1
    return s
print(sum_of_two(a=[-3,-2]))




##or 

a= int(input("enter your number: "))
b= int(input("enter your number: "))
print(a+b)