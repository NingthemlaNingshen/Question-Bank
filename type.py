bikes=int(input("enter the number of bikes : "))
cars=int(input ("enter the number of cars : "))
no_of_bikes_tyres=bikes*2
no_of_car_tyres=cars*4
print(bikes,"bikes",cars,"cars","total_no_of_tyres=",no_of_bikes_tyres+no_of_car_tyres)

## or

def faster(bikes,cars):
    x= no_of_bikes_tyres=bikes*2
    y= no_of_car_tyres=cars*4
    print(x,y) 
bikes=int(input("enter the number of bikes : "))
cars=int(input ("enter the number of cars : "))
faster(bikes,cars)