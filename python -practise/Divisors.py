num=int(input("Chose a Number: "))
listRange=list(range(1,num+1))
divisor=[]
for number in listRange:
    if num%number==0:
        divisor.append(number)
print(divisor)