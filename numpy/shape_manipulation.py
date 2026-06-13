import numpy as np



#Reshaping arrays
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:", arr)
print("Shape of Original Array:", arr.shape)

reshaped_arr = arr.reshape(2, 3)
print("\nReshaped Array (2, 3):\n", reshaped_arr)
print("Shape of Reshaped Array:", reshaped_arr.shape)

#Flattening arrays
flattened_arr = reshaped_arr.flatten()
print("\nFlattened Array:", flattened_arr)
print("Shape of Flattened Array:", flattened_arr.shape)


#raveling arrays
raveled_arr = reshaped_arr.ravel()
print("\nRaveled Array:", raveled_arr)
print("Shape of Raveled Array:", raveled_arr.shape)


#Transposing arrays
transposed_arr = reshaped_arr.T
print("\nTransposed Array:\n", transposed_arr)
print("Shape of Transposed Array:", transposed_arr.shape)


#resizing arrays
resized_arr = np.resize(arr, (3, 4))
print("\nResized Array (3, 4):\n", resized_arr)


#automatic reshaping with -1
auto_reshaped_arr = arr.reshape(-1, 2)
print("\nAutomatically Reshaped Array (-1, 2):\n", auto_reshaped_arr)
print("Shape of Automatically Reshaped Array:", auto_reshaped_arr.shape)


#Stacking arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
stacked_arr = np.stack((arr1, arr2), axis=0)
print("\nStacked Array (axis=0):\n", stacked_arr)
print("Shape of Stacked Array:", stacked_arr.shape)

#Vertical stacking
vstacked_arr = np.vstack((arr1, arr2))
print("\nVertically Stacked Array:\n", vstacked_arr)
print("Shape of Vertically Stacked Array:", vstacked_arr.shape)

#Horizontal stacking
hstacked_arr = np.hstack((arr1, arr2))
print("\nHorizontally Stacked Array:\n", hstacked_arr)
print("Shape of Horizontally Stacked Array:", hstacked_arr.shape)

#Depth stacking
dstacked_arr = np.dstack((arr1, arr2))
print("\nDepth Stacked Array:\n", dstacked_arr)
print("Shape of Depth Stacked Array:", dstacked_arr.shape)

#Concatenating arrays
concatenated_arr = np.concatenate((arr1, arr2))
print("\nConcatenated Array:", concatenated_arr)
print("Shape of Concatenated Array:", concatenated_arr.shape)


#Splitting arrays
split_arr = np.array([1, 2, 3, 4, 5, 6])
print("\nOriginal Array for Splitting:", split_arr)
split_arr1, split_arr2 = np.split(split_arr, 2)
print("Split Array 1:", split_arr1)
print("Split Array 2:", split_arr2)


#Splitting arrays with indices
split_arr3, split_arr4 = np.split(split_arr, [4])
print("\nSplit Array 3:", split_arr3)
print("Split Array 4:", split_arr4)


#Splitting arrays with equal parts
split_arr5, split_arr6, split_arr7 = np.split(split_arr, 3)
print("\nSplit Array 5:", split_arr5)
print("Split Array 6:", split_arr6)
print("Split Array 7:", split_arr7)

#hSplitting arrays
hsplit_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nOriginal Array for hSplitting:\n", hsplit_arr)
hsplit_arr1, hsplit_arr2, hsplit_arr3 = np.hsplit(hsplit_arr, 3)
print("hSplit Array 1:\n", hsplit_arr1)
print("hSplit Array 2:\n", hsplit_arr2)
print("hSplit Array 3:\n", hsplit_arr3)

#vSplitting arrays
vsplit_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nOriginal Array for vSplitting:\n", vsplit_arr)
vsplit_arr1, vsplit_arr2, vsplit_arr3 = np.vsplit(vsplit_arr, 3)
print("vSplit Array 1:\n", vsplit_arr1)
print("vSplit Array 2:\n", vsplit_arr2)
print("vSplit Array 3:\n", vsplit_arr3)

#Tiling arrays
tiled_arr = np.tile(arr1, (2, 3))
print("\nTiled Array (2, 3):\n", tiled_arr)