# Finding number of digits

num =  int (input("enter a number "))
list=[]
sum = 0
sum2 = 0
while num > 0:
    digits = num % 10
    list.append(digits)
    num = num // 10
print (len(list)    

# reversing the given number
# after finding the digits
  
list.reverse()          
for i in range(len(list)):
    sum2 = sum2 + list[i]*10**i
print (sum2)    
