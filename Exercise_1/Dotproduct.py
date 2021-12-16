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
R2 = int(input("Enter the number of rows of second matrix:"))
C2 = int(input("Enter the number of columns of second matrix:"))
  
  
print("Enter the entries  of second matrix in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrix2 = np.array(entries).reshape(R2, C2)
print(matrix2)
if(C!=R2):
    print("Matrix dot operation can't done :")
else:
    c=np.dot(matrix1,matrix2)  
    print("Dot Product of 2 matrices")
    print(c)
