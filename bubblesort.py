# Bubble sort without optimization
numbers = [5,4,3,2,1]
i = 1
while i < len(numbers):
    j=0
    while j < len(numbers)-1:
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers [j]= numbers[j+1]
            numbers[j+1]= temp
        
        j +=1
    
    i+=1        
print (numbers)
