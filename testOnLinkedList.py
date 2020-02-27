def isOperator(arg):
    operatorList=["+","-","/","*","%","(",")"]
    if arg in operatorList:
        return True
    else:
        return False
print(isOperator("+"))
print(isOperator("1"))