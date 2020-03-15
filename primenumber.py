# Finding prime numbers between 1 and 100

# num = int(input("enter a number "))
for num in range(1,101):        
    for i in range(2,num//2):
        if num % i == 0:
            # print (num,"is not prime", "first divisor is",i)
            break
    else :
        print (num,"is prime")    
 
