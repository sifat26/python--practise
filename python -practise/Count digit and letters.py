s=input("Input a string: ")
d=l=0;
for c in s:
    if c.isdigit():
        d=d+1;
    elif c.isalpha():
        l=l+1;
    else :
        pass
print("Number of letters: ",l)
print("Number of Digit: ",d)