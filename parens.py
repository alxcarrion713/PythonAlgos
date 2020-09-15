def parenvalid(stringInput):
    # your code here 
    opencount = 0
    closedcount = 0
    for i in range(0, len(stringInput), 1):
        if stringInput[i] == "(":
            opencount += 1
        elif stringInput[i]== ")":
            opencount != 0
                return False
            opencount -= 1
    if opencount >0:
        return False
    else:
        return True
print(parenvalid("()(()"))



# "()())" - false - uneven matching - 1
# "())(" - false - premature closing parens - 2
# "(())()" - true 

# 1. number of open parens must be equal to number of closed parens
# 2. closing parens cannot come prematurely