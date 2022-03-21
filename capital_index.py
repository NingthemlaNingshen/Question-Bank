def capital_indexes(chr):
    i=0
    a=[]
    while i<len(chr):
        if chr[i]<="Z":
            a.append(i)
        i=i+1
    return a
print(capital_indexes(chr=input("enter your chr: ")))