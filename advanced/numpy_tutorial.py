import numpy as np

# create one-dimensional array with five elements
a = np.array([1, 2, 3, 4, 5])
print("Array a:", a)

# create 2D array (matrix) of shape 3x3
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Matrix b:\n", b)

# array attributes
print("Shape of b:", b.shape)
print("Number of dimensions of b:", b.ndim)
print("Data type of b elements:", b.dtype)
# convert to float type
b = b.astype(float)
print("Converted matrix b to float, new dtype:", b.dtype)

# indexing and slicing
print("b[0, 0]:", b[0, 0])
print("First row of b:", b[0, :])
print("Second column of b:", b[:, 1])
# slicing with step
print("Elements of a with step 2:", a[::2])

# basic array operations
sum_array = a + np.array([5, 5, 5, 5, 5])  # adding two arrays
print("a + [5,5,5,5,5]:", sum_array)

scaled = a * 2  # element-wise multiplication by scalar
print("a * 2:", scaled)

# matrix multiplication (dot product)
c = np.dot(b, b)
print("Dot product b * b:\n", c)

# sum of elements
print("Sum of elements in a:", a.sum())
print("Sum of each column in b:", b.sum(axis=0))
# example of an invalid axis in sum (to show an error)
try:
    print("Sum with invalid axis 2:", b.sum(axis=2))
except Exception as e:
    print("Error summing along axis 2 (invalid):", e)

# use of universal functions (ufuncs)
d = np.array([0, np.pi/2, np.pi])
print("Angles d:", d)
print("sin(d):", np.sin(d))
print("log of d (with -inf for zero):", np.log(d))

# broadcasting example
e = np.arange(1, 4)
f = np.array([[1], [2], [3]])
print("e:", e)
print("f:", f)
print("Broadcasted sum e+f:\n", e + f)

# reshape example
g = np.arange(8)
g = g.reshape((2,4))
print("Reshaped g to 2x4:\n", g)

# simple statistics
print("Mean of a:", a.mean())
print("Standard deviation of g:", g.std())

# find unique elements
h = np.array([1, 2, 2, 3, 3, 3])
print("Unique elements in h:", np.unique(h))

# sort elements of an array in descending order
print("Sorted a in descending:", np.sort(a)[::-1])

# random array example
np.random.seed(0)
rand_arr = np.random.rand(3, 3)
print("Random array:", rand_arr)

# element-wise comparison
print("Elements of rand_arr > 0.5:\n", rand_arr > 0.5)

# creating arrays using linspace
lin = np.linspace(0, 1, 5)
print("Linearly spaced array:", lin)
