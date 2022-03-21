# Power of Four
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.


def Power_of_four(num):
    if (num == 0):
        return False
    while (num != 1):
        if (num % 4 != 0):
            return False
        num = num // 4
    return True
num = int(input("enter your number: "))
if(Power_of_four(num)):
    print(num, 'is a power of 4')
else:
    print(num, 'is not a power of 4')


