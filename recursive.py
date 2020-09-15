def factorial(numinput):
    if numinput<=1:
        return 1
    else:
        return numinput * factorial(numinput-1)

print(factorial(4))