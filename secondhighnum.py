# to find the second highest number in the given string
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]

# by using two loops
j=0
index = 0
for i in range (len(numbers)):
    if j< numbers[i]:
        j = numbers[i]
        index = i
numbers.pop(index) 
s=0
for i in range(len(numbers)):
    if s < numbers[i]:
        s = numbers[i]
print (s)

# by using one loop

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]

# initialize with least number possible
first_max = 0
sec_max = 0

for i in numbers:
    if first_max < i :
        sec_max = first_max
        first_max = i
    if sec_max < i and first_max > i:
        sec_max = i
print (sec_max)




