import numpy as np


input1 = input("Enter the elements of the first array (separated by spaces): ")
array1 = np.array([x for x in input1.split()])


input2 = input("Enter the elements of the second array (separated by spaces): ")
array2 = np.array([x for x in input2.split()])


if np.array_equal(array1, array2):
	print("arrays are equel")
	
else:
	perint('arrays are not equel')

