
import numpy as np

#advanced indexing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:\n", arr)
#Using integer array indexing
row_indices = np.array([0, 1, 2])
col_indices = np.array([2, 1, 0])
result = arr[row_indices, col_indices]
print("Result of Integer Array Indexing:\n", result)


#Using boolean array indexing
bool_indices = arr > 5
result2 = arr[bool_indices]
print("Result of Boolean Array Indexing:\n", result2)

#Using fancy indexing
fancy_indices = [0, 2]
result3 = arr[fancy_indices, :]
print("Result of Fancy Indexing:\n", result3)


#ix_ function
row_indices2 = np.array([0, 1])
col_indices2 = np.array([1, 2])
result4 = arr[np.ix_(row_indices2, col_indices2)]
print("Result of ix_ function:\n", result4) 