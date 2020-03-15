# python program to check whether the number is armstrong or not

num =  int (input("enter a number "))
num1 = num
list=[]
sum = 0

# finding the number of digits in the given number
# by adding the elements in list
while num1 > 0: 
    digits = num1 % 10
    list.append(digits)
    num1 = num1 // 10
print (list) 
for i in range(len(list)):
    sum = sum + list[i]**len(list)
if sum == num:
    print ("armstrong number")
else:
    print ("sorry not an armstrong number")          

