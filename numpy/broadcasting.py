
import numpy as np

#Broadcasting
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

# Broadcasting arr2 to match the shape of arr1
result = arr1 + arr2
print("Result of Broadcasting:\n", result)


#single dimensional broadcasting
arr3 = np.array([1, 2, 3])
arr4 = np.array([[10], [20], [30]])
print("\nArray 3:\n", arr3)
print("Array 4:\n", arr4)
result2 = arr3 + arr4
print("Result of Broadcasting (Single Dimensional):\n", result2)

#ufunc broadcasting
arr5 = np.array([[1, 2, 3], [4, 5, 6]])
arr6 = np.array([10, 20, 30])
print("\nArray 5:\n", arr5)
print("Array 6:\n", arr6)
result3 = np.add(arr5, arr6)
print("Result of Broadcasting using ufunc:\n", result3)


#Broadcasting with different shapes
arr7 = np.array([[1, 2], [3, 4], [5, 6]])
arr8 = np.array([10, 20])
print("\nArray 7:\n", arr7)
print("Array 8:\n", arr8)
result4 = arr7 + arr8
print("Result of Broadcasting with Different Shapes:\n", result4)