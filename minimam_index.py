
# ### part 1
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
i=0
while i<len(list1):
    j=0
    while j<len(list2):
        if list1[i]==list2[j]:
            print(list1[i])
        j+=1   
    i=i+1

# ##part2

list1 = ["KFC","Shogun","Tapioca Express","Burger King"]
list2 = ["Piatti","The Grill at Torrey Pines","KFC","Hungry Hunter Steakhouse","Shogun"]
i=0
c=0
a=[]
while i<len(list1):
    j=0
    while j<len(list2):
        if list1[i]==list2[j]:
            c=i+j
            a.append(list1[i])
            a.append(c)  
        j+=1
    i=i+1
print(a)




#### or

list1 = ["Tapioca Express","Piatti","Shogun","Burger King","KFC"]
list2 = ["KFC","Piatti","The Grill at Torrey Pines","Shogun","Hungry Hunter Steakhouse"]
i=0
a=[]
while i<len(list1):
    j=0
    b=[]
    while j<len(list2):
        if list1[i]==list2[j]:
            c=i+j
            b.append(list1[i])
            b.append(c) 
        j+=1
    if len(b)>0:
        a.append(b)
    i=i+1
print(a)
k=0
while k<len(a):
    l=0
    while l<len(a):
        if a[k][1]>a[l][1]:
            print(a[l][0],"has the minimum index sum")
            break
        else:
            print(a[k][0],"has the minimum index sum")
            break
        l=l+1
    break
    k=k+1
