user=int(input("enter your number: "))
i=0
a=[]
b=""
while i<user:
    array=int(input("enter your number: "))
    a.append(array)
    j=0
    while j<len(a):
        num=a[j]%10
        j=j+1
    b=b+str(num) 
    i=i+1
if int(b)/10==0:
    print(b,"is divisible by 10 ",True)
else:
    print(b,"is not divisible by 10 ",False)


### or

array=[85,25, 65, 21, 84]
i=0
b=""
while i<len(array):
    a=array[i]%10
    b+=str(a)   
    i=i+1
if int(b)/10==0:
    print(b, "Yes")
else:
    print(b, "No")
