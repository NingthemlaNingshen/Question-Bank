def is_anagram(a,b):
    if sorted(a)== sorted(b):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.") 
is_anagram("typhoon","opython") 

## or

def is_anagram():
    if sorted(a)== sorted(b):
        print(True)
    else:
        print(False) 
a=input("enter your charecter: ")
b=input("enter your charecter: ")
is_anagram()