from stacKUsingLinkedList import Stack
operatorPre={"+":0,"-":0,"/":1,"*":1,"%":1,"(":2,")":2}
def isOperator(arg):
    operatorList=["+","-","/","*","%","(",")"]
    if arg in operatorList:
        return True
    else:
        return False

def InfixToPostfix(string):
    if isOperator(string[0]):
        return None
    stack=Stack()
    string=string.split(" ")
    length=len(string)
    eqution=""
    for i in range(length):
        if not isOperator(string[i]): #operand or not
            eqution=eqution+string[i]+" "
        #it is an operator but not ( not )
        if isOperator(string[i]) and string[i]!="(" and string[i]!=")":
            #if stack is not empty
            #is top element is not (
            #if precedence of top > scanning element
            while not stack.isEmpty() and stack.peek()!="(" and operatorPre[stack.peek()]>operatorPre[string[i]]:
                eqution=eqution+stack.peek()+" "
                stack.pop()
            #otherwise
            stack.push(string[i])
        #operator and (
        if string[i]=="(":
            stack.push(string[i])
        #operator and )
        if string[i]==")":
            while not stack.isEmpty() and stack.peek()!="(": #when u get ) pop out everything until get (
                eqution=eqution+stack.peek()+" "
                stack.pop()
            stack.pop() #pop out (
    while not stack.isEmpty(): #pop out remaining from stack
        eqution=eqution+stack.peek()+" "
        stack.pop()
    return eqution
def InfixToPrefiX(string):
    if isOperator(string[0]):
        return None
    string=string[::-1]  #reversing the string
    string=InfixToPostfix(string)
    string=string[::-1]   #reversing the string
    string=string[1:] #1st space removal during reversing
    return string
def PostFixToInfix(string):
    if isOperator(string[0]):
        return None
    stack=Stack()
    string=string.split(" ")
    length=len(string)
    eqution=""
    for i in range(length):
        #operand
        if not isOperator(string[i]):
            stack.push(string[i])
        #operator
        else:
            a=stack.pop()
            b=stack.pop()
            eqution=eqution+b+" "+string[i]+" "+a
            stack.push(eqution)
            eqution=""
    eqution=stack.pop()
    return eqution
def PreFixToInfix(string):
    if not isOperator(string[0]):
        return None
    stack=Stack()
    string=string.split(" ")
    length=len(string)
    eqution=""
    i=length-1
    while i>=0:
        #operand
        if not isOperator(string[i]):
            stack.push(string[i])
        #operator
        else:
            a=stack.pop()
            b=stack.pop()
            eqution=eqution+a+" "+string[i]+" "+b
            stack.push(eqution)
            eqution=""
        i-=1
    eqution=stack.pop()
    return eqution
def PreFixToPostFix(string):
    if not isOperator(string[0]):
        return None
    string=PreFixToInfix(string)
    string=InfixToPostfix(string)
    return string
def PostFixToPreFix(string):
    if isOperator(string[0]):
        return None
    string=PostFixToInfix(string)
    string=InfixToPrefiX(string)
    return string


print(InfixToPostfix("7 + 8 * 9"))
print(InfixToPrefiX("7 + 8 * 9"))
print(PreFixToPostFix("+ 7 * 8 9"))
print(PostFixToPreFix("7 8 9 * +"))
print(PostFixToPreFix("+ 7 * 8 9"))
