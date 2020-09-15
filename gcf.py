def computegcd(x,y):
    while (y):
        x, y = y, x % y

    return x

a= 60
b= 48

print(computegcd(60,48))

