# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should
#  extract and return the middle letter. If there is no middle letter, your function should 
# return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".
def mid(chr):
    i=0
    while i<len(chr):
        if len(chr)%2==0:
            return ""
        else:
            m=len(chr)//2
            return chr[m]
        i=i+1
print(mid(chr=input("enter your chr: ")))