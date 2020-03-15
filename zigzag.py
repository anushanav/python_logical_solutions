# Printing numbers in zigzag diagonally pattern in n*n matrix

# This is code I had written in the early phase of coding,
#  hence a very naive approach.

matrix =[[0] * 3 for i in range(3)]
starting_row = 0 
starting_column = 0
ending_row = 3
ending_column = 3
column = 0

num = 1
while column < ending_column:
    if column % 2 == 0:
        i = column
        j = 0
        while i >= starting_row and j< ending_column:
            matrix[i][j]=num
            num +=1
            i -= 1
            j += 1
    
    column += 1
    if not column < ending_column:
        break
    if column % 2 ==1:
        i = 0
        j = column
        while i < er and j>= starting_column:
            matrix [i][j] = num
            num += 1
            i += 1
            j -= 1
    column += 1

# Printing done till the major diagonal now the direction changes according 
# to which column ended
rows = 1   
if column % 2 == 1:
    while rows < er:
        i = rows
        j = ending_column -1
        while i < er :
            matrix [i][j] = num
            num += 1
            i += 1
            j -= 1
        
        rows += 1
        if not rows < er:
            break
        
        i = er-1
        j = rows
        while  j< ending_column:
            matrix[i][j]=num
            num +=1
            i -= 1
            j += 1
        rows +=1
    
else :
    while rows < er:
        i = er-1
        j = rows
        while  j< ending_column:
            matrix[i][j]=num
            num +=1
            i -= 1
            j += 1
        
        rows += 1
        if not rows < er:
            break
        
        i = rows
        j = ending_column -1
        while i < er :
            matrix [i][j] = num
            num += 1
            i += 1
            j -= 1
        
        rows += 1
        
print (matrix)