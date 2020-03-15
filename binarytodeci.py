def binaryToDeci (num):
    number = 0
    j = 0
    for i in range(len(num)-1,-1,-1):
        number += 2**j * int(num[i])
        j += 1
    return number

solve = binaryToDeci("01001000")
print (solve)

