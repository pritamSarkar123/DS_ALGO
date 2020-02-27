###################### memoization by inbuilt func##########
from functools import lru_cache
@lru_cache(maxsize=1000)      #bydefault 128 recent calls
def fibonacci(n): #returns the n th fibonacchi tearm
    if type(n)!=int:
        raise TypeError("not of int type!")
    if n<1:
        raise ValueError("not correct value")
    if n==1:
        return 1
    elif n==2:
        return 2 
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
for i in range(1,101):
    print(fibonacci(i+1))

#print(fibonacchi(i+1)/fibonacchi(i))  #time quantum