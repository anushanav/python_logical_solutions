l= 1
while l < 6:
    k = 1
    while k < l+ 1:
        print (k , " ", end= "")
        k += 1

    print ()
    l += 1


i= 1
counting = 1
while i < 6:
    j =1
    while j < i+ 1:
        print (counting , " ", end= "")
        counting +=1
        j += 1

    print ()
    i += 1


m = 1
for i in range (1,6):
    print (str(i)*i)