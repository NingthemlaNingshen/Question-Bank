nums = [0,1,0,3,12]
i=0
while i<len(nums):
    j=0
    while j<len(nums)-1:
        if nums[j]==0:
            nums[j],nums[j+1]=nums[j+1],nums[j]
        j=j+1
    i=i+1
print(nums)


### or

nums = [0,1,0,3,12]
i=0
a=[]
b=[]
while i<len(nums):
    if nums[i]==0:
        a.append(nums[i])
    else:
        b.append(nums[i])
    i=i+1
b.extend(a)
print(b)


### or

def move_Zeros(list):
    i=0
    while i<len(list):
        j=0
        while j<len(list)-1:
            if list[j]==0:
                list[j],list[j+1]=list[j+1],list[j]
            j=j+1
        i=i+1
    print(list)
move_Zeros(list=[1,4,0,7,0,3])