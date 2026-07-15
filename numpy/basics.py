
import numpy as np



#basic array creation

arr1 = np.array([1,2,3,4,5])

print("Array 1:", arr1)

print("Shape of Array 1:", arr1.shape)
print("Data type of Array 1:", arr1.dtype)
print(type(arr1))


empty = np.empty((2, 3))
print("\nEmpty Array:\n", empty)
print("Shape of Empty Array:", empty.shape)
print("Data type of Empty Array:", empty.dtype)


#basic array creation with zeros
zeros = np.zeros((3, 4))
print("\nArray of zeros:\n", zeros)

#basic array creation with ones
once = np.ones((4, 5))
print("\nArray of ones:\n", once)


#2d array creation
arr2d = np.array([[1,2,3],[4,5,6],[7,8,3]])
print("\n2D Array:\n", arr2d)
print("Shape of 2D Array:", arr2d.shape)
print("Data type of 2D Array:", arr2d.dtype)
print(type(arr2d))

print(arr2d.size)  # Total number of elements

print(arr2d.ndim)  # Number of dimensions

print(arr2d.itemsize)  # Size of each element in bytes

print(arr2d.nbytes)  # Total size of the array in bytes

print(arr2d.T)  # Transpose of the array

print(arr2d.data)  # Accessing the underlying data buffer



arrs = np.array([(1, 2, 3), (4, 5, 6)])
print("\nStructured Array:\n", arrs)


#arange
arr_arange = np.arange(0, 10, 3)
print("\nArray created using arange:\n", arr_arange)

#linspace
#How linspace works: It generates a specified number of evenly spaced values between a given start and end point. The syntax is np.linspace(start, stop, num), where 'start' is the beginning of the interval, 'stop' is the end of the interval, and 'num' is the number of values to generate. The generated values include both the start and stop points by default.
arr_linspace = np.linspace(0, 1, 5)
print("\nArray created using linspace:\n", arr_linspace)