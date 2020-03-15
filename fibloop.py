# Fibonnaci series
a = 0
b = 1
fib =[]
for i in range(10):
    fib.append(a)
    fib.append(b)
    a = a + b
    b = b + a
print (fib)

# Fibonnaci recursion way
def fib_recursion(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_recursion(n-1)+fib_recursion(n-2)




