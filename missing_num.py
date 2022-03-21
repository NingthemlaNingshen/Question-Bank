# Min-maxing
# Define a function named largest_difference that takes a list of numbers as its only parameter.
# Your function should compute and return the difference between the largest and smallest number 
# in the list.
# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
# You may assume that no numbers are smaller or larger than -100 and 100.
def largest_difference(list):
    i=0
    m=0
    s=list[0]
    while i<len(list):
        if list[i]>m:
            m=list[i]
        if list[i]<s and m>list[i]:
            s=list[i]
        i=i+1
    return m-s
print(largest_difference(list=[1, 5, 2, 3]))