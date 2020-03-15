# Printing mirror image of the given matrix
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
mirror= [[0]*3 for i in range(3)]

rows = 3
columns = 3

for i in range(rows):
    for j in range(columns):
        mirror[i][j]=matrix[i][columns-1-j]


# printing a matrix that shows addition of the given matrix and its mirror 
solution=[[0]*3 for i in range(3)]

for i in range(rows):
    for j in range(columns):
        solution[i][j]= matrix[i][j]+ matrix[i][columns-1-j]
        
print (solution)
