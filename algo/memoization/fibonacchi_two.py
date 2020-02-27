fibonacchi_cahce={}
def fibonacci(n): #returns the n th fibonacchi tearm
    if type(n)!=int:
        raise TypeError("not of int type!")
    if n<1:
        raise ValueError("not correct value")
    if n in fibonacchi_cahce: #if present in cache
        return fibonacchi_cahce[n]
    else: #if not present in cache
        if n==1:
            value=1
        elif n==2:
            value=2 
        else:
            value=fibonacci(n-1)+fibonacci(n-2)
        fibonacchi_cahce[n]=value
        return value
for i in range(1,101):
    print(fibonacci(i))

#print(fibonacchi(i+1)/fibonacchi(i))  #time quantum

