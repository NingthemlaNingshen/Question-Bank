# Length of Number

def number(num):
    i=0
    while num[i:]:
        i=i+1
    return i
print(number(num=input("enter your number: ")))