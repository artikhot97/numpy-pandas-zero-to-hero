import numpy as np

#views and copies
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
#Creating a view -> shallow copy
view_arr = arr.view()
print("View of the Array:", view_arr)
#Modifying the view
view_arr[4] = 10
print("Modified View Array:", view_arr)
print("Original Array after modifying the view:", arr)  # Original array is also modified

#Creating a copy -> deep copy
copy_arr = arr.copy()
print("Copy of the Array:", copy_arr)
#Modifying the copy
copy_arr[0] = 100
print("Modified Copy Array:", copy_arr)
print("Original Array after modifying the copy:", arr)  # Original array remains unchanged


