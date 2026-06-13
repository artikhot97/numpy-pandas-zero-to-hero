import numpy as np

#Single Dinsional Array Creation
#Mathematical operations 

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)
#Addition
add = arr1 + arr2
print("Addition of arr1 and arr2:", add)


#Subtraction
sub = arr2 - arr1
print("Subtraction of arr1 from arr2:", sub)

sub1 = arr2
sub1 -= arr1
print("Subtraction of arr1 from arr2 (using in-place operation):", sub1)

#Multiplication
mul = arr1*arr2
print("Multiplication of arr1 and arr2:", mul)


#Division
div = arr2 / arr1
print("Division of arr2 by arr1:", div)


#upcasting
arr3 = np.array([1, 2, 3], dtype=np.int32)
arr4 = np.array([1.5, 2.5, 3.5], dtype=np.float64)

result = arr3 + arr4
print("Result of adding arr3 and arr4 (upcasting to float64):", result)
print("Data type of the result:", result.dtype)

result2 = arr3 * arr4
print("Result of multiplying arr3 and arr4 (upcasting to float64):", result2)
print("Data type of the result:", result2.dtype)



#Unary operations
arr5 = np.array([-1, -2, -3, -4, -5])
print("Array 5:", arr5)
abs_arr5 = np.abs(arr5)
print("Absolute values of arr5:", abs_arr5)

min_arr5 = np.min(abs_arr5)
print("Minimum value in arr5:", min_arr5)

max_arr5 = np.max(abs_arr5)
print("Maximum value in arr5:", max_arr5)

#How mean is calculated -> sum of all elements / number of elements
mean_arr5 = np.mean(abs_arr5)
print("Mean value of arr5:", mean_arr5)

#sunm of all elements
sum_arr5 = np.sum(abs_arr5)
print("Sum of all elements in arr5:", sum_arr5)


#axis parameter in aggregation functions
#How axis parameter works -> axis parameter specifies the axis along which the aggregation function is applied. For example, if we have a 2D array and we want to calculate the sum along the columns, we can use axis=0. If we want to calculate the sum along the rows, we can use axis=1.
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", arr2d)
sum_axis0 = np.sum(arr2d, axis=0)
print("Sum along axis 0 (columns):", sum_axis0)

sum_axis1 = np.sum(arr2d, axis=1)
print("Sum along axis 1 (rows):", sum_axis1)

#Universal functions (ufuncs)
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
squared_arr = np.square(arr)
print("Squared Array:", squared_arr)

#sine of the array
#How sine is calculated -> sine of each element in the array
#formula for sine -> sine of x = opposite / hypotenuse 
#example -> sine of 30 degrees = 0.5 (opposite side is 1 and hypotenuse is 2)
#how sine is calculated in numpy -> sine of each element in the array is calculated using the formula sine of x = opposite / hypotenuse example -> sine of 30 degrees = 0.5 (opposite side is 1 and hypotenuse is 2) and the result is stored in a new array called sine_arr 
# sin of array is calculated using the formula sine of x = opposite / hypotenuse example -> sine of 30 degrees = 0.5 (opposite side is 1 and hypotenuse is 2) and the result is stored in a new array called sine_arr
#calculation ex for arr  1
sine_arr = np.sin(arr)
print("Sine of the array:", sine_arr)

#How cosine is calculated -> cosine of each element in the array is calculated using the formula cosine of x = adjacent / hypotenuse example -> cosine of 30 degrees = 0.866 (adjacent side is 1 and hypotenuse is 2) and the result is stored in a new array called cos_arr
cos_arr = np.cos(arr)
print("Cosine of the array:", cos_arr)

#tangent of the array
#How tangent is calculated -> tangent of each element in the array is calculated using the formula tangent of x = opposite / adjacent example -> tangent of 30 degrees = 0.577 (opposite side is 1 and adjacent side is 1.732) and the result is stored in a new array called tan_arr
tan_arr = np.tan(arr)
print("Tangent of the array:", tan_arr)

#exponential of the array
#How exponential is calculated -> exponential of each element in the array is calculated using the formula e
exp_arr = np.exp(arr)
print("Exponential of the array:", exp_arr)

#Univasriate functions
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
sqrt_arr = np.sqrt(arr)
print("Square root of the array:", sqrt_arr)


#Logical operations
arr6 = np.array([1, 2, 3, 4, 5])
arr7 = np.array([5, 4, 3, 2, 1])
greater_than = arr6 > arr7
print("Element-wise comparison (arr6 > arr7):", greater_than)