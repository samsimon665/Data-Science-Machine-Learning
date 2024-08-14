import numpy as np


size = int(input("Enter the size of the square matrix: "))
m1 = []

print("Enter each row of the matrix, with elements separated by spaces:")


for i  in range(size):
    row = list(map(int, input().split()))
    m1.append(row)


print('1. sum of elements :',np.sum(m1))

print('1. sum of rows :',np.sum(m1,axis=1))

print('1. sum of columns :',np.sum(m1,axis=0))


