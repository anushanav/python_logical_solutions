# Printing numbers in a spiral pattern in a matrix of n*n

n = int(input("enter a number "))

matrix = [[0] * n for i in range(n)]
# sr = starting row , sc = starting column , er = ending row , ec = ending column
sr = 0      
sc = 0
er = n
ec = n
num = 1

while sr < er and sc < ec:
    for i in range(sc,ec,1):
        matrix[sr][i] = num
        num += 1
    sr += 1

    for i in range(sr,er,1):
        matrix[i][ec-1]= num
        num += 1
    ec -= 1

    for i in range(ec-1,sc-1,-1):
        matrix[er-1][i] = num
        num += 1
    er -= 1

    for i in range(er-1,sr-1,-1):
        matrix[i][sc] = num
        num += 1
    sc += 1
    
print (matrix)