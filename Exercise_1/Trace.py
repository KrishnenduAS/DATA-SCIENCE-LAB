import numpy as np
  
R = int(input("Enter the number of rows of first matrix:"))
C = int(input("Enter the number of columns of first matrix:"))
  
  
print("Enter the entries  of first matrix in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix1= np.array(entries).reshape(R, C)
print(matrix1)
c=np.trace(matrix1)  
print("Trace  of  matrices")
print(c)
