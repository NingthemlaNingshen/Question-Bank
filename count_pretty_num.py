user=int(input("enter your number: "))
i=int(input("enter your number: "))
c=0
while i<=user:
    if i%10==2 or i%10==3 or i%10==9:
        c=c+1
    i=i+1
print(c,"pretty numbers are there in ",i,"to",user)
