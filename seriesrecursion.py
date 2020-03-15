# If n is odd then nth element is double of (n-1) element
# If n is even then nth element is obtained by adding 3 to n-1 element

def seriesWeird (n):
    if n== 1:
        return 1
    else:
        if n%2 == 1:
            return seriesWeird(n-1)*2
        else:
            return seriesWeird(n-1)+3
            
            
i = 1
while i<10:
    print (seriesWeird(i), end=" ")
    i += 1
        

# If n is odd then nth element is 10 times the (n-1) element
# If n is even then nth element is obtained by adding 1 to n-1 element
def seriesWeird2 (n):
    if n== 1:
        return 10
    else:
        if n%2 == 1:
            return seriesWeird2(n-1)*10
        else:
            return seriesWeird2(n-1)+1
            
            
i = 1
while i<10:
    print (seriesWeird2(i), end=" ")
    i += 1
        