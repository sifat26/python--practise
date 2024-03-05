weight=int(input("Weight"))
format=input("(K)g or (L)bs")
if format.lower()=="k":
    print("Weight: ",weight/0.45)
else:
    print("Weight: ",weight*0.45)

