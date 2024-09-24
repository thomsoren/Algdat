def fib(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    



# Fibonachi rekken: 1 1 2 3 5 8 

print(fib(6))
    