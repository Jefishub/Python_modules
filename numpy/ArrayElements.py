# Access Array Elements
import numpy as np

arr2 = np.arange(start=1, stop=7)
arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr2)
print(arr2[3])
print(arr2.ndim)

print("Whole array")
print(arr3)
print("Accessing")
print(arr3[0,2])
print("Slicing")
print(arr3[0][1:3])
print(arr3[0][1:-1])