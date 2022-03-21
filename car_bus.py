CAR=int(input("CAR takes: "))
BIKE=int(input("BIKE takes: "))
if CAR>BIKE:
    print("bike is faster")
elif CAR<BIKE:
    print("car is faster")
else:
    print("will reach at the same time")


### or
def faster():
    if CAR>BIKE:
        print("bike is faster")
    elif CAR<BIKE:
        print("car is faster")
    else:
        print("will reach at the same time")
CAR=int(input("CAR takes: "))
BIKE=int(input("BIKE takes: "))
faster()


## or 
car=[2,3,4,6]
bike=[1,2,4,7]
i=0
while i<len(car):
    if car[i]<bike[i]:
        print("car is faster")
    if car[i]>bike[i]:
        print("bike is faster")
    else:
        print("will reach at the same time")
    i=i+1