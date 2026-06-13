import numpy as np

#Basic slicing and indexing

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

#Slicing
slice_arr = arr[1:4]
print("Sliced Array (1:4):", slice_arr)
print(slice_arr.base)  # Shows that slice_arr is a view of arr
"""why output is [3 4] and not [2 3] -> because the original array is [1, 2, 3, 4, 5] 
and we are slicing from index 1 to index 4 (exclusive) which gives us [2, 3, 4]. Then we are slicing this sliced array from index 1 to index 3 (exclusive) which gives us [3, 4].
"""
print(slice_arr[1:3])  # Further slicing of the sliced array



#Indexing
index_arr = arr[2]
print("Indexed Array (index 2):", index_arr)

# #Multidimensional slicing and indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:\n", arr2d)

# #Slicing
slice_arr2d = arr2d[0:2, 1:3]
print("Sliced 2D Array (0:2, 1:3):\n", slice_arr2d)

#Indexing
index_arr2d = arr2d[1, 2]
print("Indexed 2D Array (1, 2):", index_arr2d)


#Iteration
print("\nIterating over 2D Array:")
for row in arr2d:
    print(row)
    