import numpy as np

#creating 1D array
arrOne = np.array([1, 2, 3])
print("\n one dimension :", arrOne)

arrTwo = np.array([['apple', 'mango','banana'], ['kivi', 'blueberry', 'orange']])
print("\n two dimension :\n",arrTwo)

arrThree = np.array([[[12, 13, 14], [13, 14, 15], [16, 17, 18]]])
print("\n three Dimension :\n",arrThree)


#only rows
print("\n Shape : \n",arrOne.shape)

#rows and Colums
print(arrTwo.shape)

#blocks and rows and columns
print(arrThree.shape)


print("\n size means number of Dimensions in Array :")
print(arrOne.ndim)
print(arrTwo.ndim)
print(arrThree.ndim)

print("\n size means number of elements in Array :")
print(arrOne.size)
print(arrTwo.size)
print(arrThree.size)


print("\n Data Types in Array :")
print(arrOne.dtype)
print(arrTwo.dtype)
print(arrThree.dtype)


print("\n Items Size in array (how much memory requried to save a data type) :")
print(arrOne.itemsize)
print(arrTwo.itemsize)
print(arrThree.itemsize)


#indexing
print("\n indexing")
print(arrOne[1])
print(arrTwo[1, 2])
print(arrThree[0, 1, 2])

print(arrThree[0, 1, 2])