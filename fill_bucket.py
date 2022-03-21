capacity=int(input("enter your number: "))
filled=int(input("enter your number: "))
if capacity>filled:
    print(capacity-filled,"l can fill in the bucket without overflowing.")
else:
    print(filled-capacity,"overflowing")
