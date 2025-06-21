# 🐍 Python Basics – Day 4 Explanations

This markdown file contains explanations, code examples, and outputs for the topics learned on **Day 4**.

---

## 24. 📦 Array in Python (Using List)

### ✅ Code
```python
arr = [10, 20, 30, 40, 50]
print("Array:", arr)
```

### 🔽 Output
```
Array: [10, 20, 30, 40, 50]
```

### 📘 Explanation
- Python has no built-in array type like C/C++.
- We use **lists** to represent simple arrays.

---

## 25. 🧑‍💻 Taking Array Values from User

### ✅ Code
```python
size = int(input("Enter number of elements: "))
user_arr = []
for i in range(size):
    val = int(input(f"Enter element {i+1}: "))
    user_arr.append(val)
print("User array:", user_arr)
```

### 🔽 Output (Example)
```
Enter number of elements: 3
Enter element 1: 11
Enter element 2: 22
Enter element 3: 33
User array: [11, 22, 33]
```

### 📘 Explanation
- We take input using `input()` and store values in a list using `append()`.

---

## 26. 🤖 Why NumPy?

### ✅ Code
```python
import numpy as np
list1 = [1, 2, 3, 4]
np_arr = np.array(list1)
print("List multiplied:", list1 * 2)
print("NumPy array multiplied:", np_arr * 2)
```

### 🔽 Output
```
List multiplied: [1, 2, 3, 4, 1, 2, 3, 4]
NumPy array multiplied: [2 4 6 8]
```

### 📘 Explanation
- Multiplying a list repeats the values.
- Multiplying a NumPy array multiplies each element. ✅
- NumPy is faster, memory-efficient, and supports vectorized operations.

---

## 27. 🛠️ Ways of Creating NumPy Arrays

### ✅ Code
```python
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.zeros(3)
arr3 = np.ones(3)
arr4 = np.arange(0, 10, 2)
arr5 = np.linspace(1, 5, 4)
```

### 🔽 Output
```
Array: [1 2 3]
Zeros: [0. 0. 0.]
Ones: [1. 1. 1.]
Arange: [0 2 4 6 8]
Linspace: [1. 2.333 3.666 5.]
```

### 📘 Explanation
- `np.array()` – basic array
- `np.zeros()` – creates array of 0s
- `np.ones()` – creates array of 1s
- `np.arange(start, stop, step)` – like Python’s range()
- `np.linspace(start, stop, num)` – evenly spaced values between range

---

## 28. 📋 Copying Arrays

### ✅ Code
```python
import numpy as np
arr = np.array([1, 2, 3])
copy_arr = arr.copy()
copy_arr[0] = 100
print("Original:", arr)
print("Copy:", copy_arr)
```

### 🔽 Output
```
Original: [1 2 3]
Copy: [100   2   3]
```

### 📘 Explanation
- Use `.copy()` to make an independent copy of the array.
- Changing one does not affect the other.

---

## 29. 🧮 Matrix Operations Using NumPy

### ✅ Code
```python
import numpy as np
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
sum_mat = mat1 + mat2
prod_mat = mat1 @ mat2
```

### 🔽 Output
```
Matrix 1:
 [[1 2]
  [3 4]]
Matrix 2:
 [[5 6]
  [7 8]]
Sum:
 [[ 6  8]
  [10 12]]
Product:
 [[19 22]
  [43 50]]
```

### 📘 Explanation
- `@` operator or `np.dot()` is used for matrix multiplication.
- Works only when dimensions match (`A(m×n) * B(n×p)`).
