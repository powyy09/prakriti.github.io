def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
       return n* factorial(n-1)

print(factorial(7))

def fibonacii(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacii(n-1)+fibonacii(n-2)
    
i=0
while i<10:
    print (fibonacii(i))
    i=i+1


