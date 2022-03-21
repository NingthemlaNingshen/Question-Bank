total=int(input("Chef has to gift a total of"))
Chef_choco=int(input("Chef has "))
price=int(input("enter the price of chocolate"))
a=total-Chef_choco
b=a*price
print("Chef he has only", Chef_choco ,"But he want to give", total ,"so he need", total-Chef_choco ,"choco")
print("Chef needs to spend ", b, "so that he can gift C chocolatesto Botswal.")



## or

total=int(input("Chef has to gift a total of "))
Chef_choco=int(input("Chef has "))
price=int(input("enter the price of chocolate "))
if Chef_choco<total:
    a=total-Chef_choco
    b=a*price
    print("Chef needs to spend ", b)
else:
    print("Chef has enough choco")