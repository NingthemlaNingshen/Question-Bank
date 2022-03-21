user=int(input("enter your number: ")) 
i=0
a=[]
while i<user:
    Battery=int(input("enyer your number: "))
    a.append(Battery)
    i+=1
j=0
while j<len(a):
    if a[j]<=15:
        print(a[j],"Yes Battery low")
    else:
        print(a[j],"No")
    j+=1


## or 

user=int(input("enter you number:"))
if user>15:
    print("Battery is not low")
else:
    print("Low battery")