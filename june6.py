def coins (amountIncents):
    quarters=0
    dimes=0
    nickels=0
    pennies=0
    for i in range(0,amountIncents-24,25):
        quarters +=1
        count =25
    for i in range(count, amountIncents-9,10):
        dimes +=1
        count = 10
    for i in range(count, amountIncents-4,5):
        nickels +=1
        nickels= 5
    for i in range(count),amountIncents,1:
        pennies +=1
        pennies= 1
    objcoins={'q':quarters, 'n':nickels, 'p':pennies,'d':dimes}
    

    print({quarters,dimes,nickels,pennies})

print(coins(100))