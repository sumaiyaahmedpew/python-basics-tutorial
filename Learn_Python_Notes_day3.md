# 🐍 Python Basics – Day 3 Explanations

This markdown file contains explanations, code examples, and outputs for the topics learned on **Day 3**.

---

## 14. 🔁 Swapping Two Variables

### ✅ Code
```python
a = 5
b = 10
print("Before Swap: a =", a, ", b =", b)
a, b = b, a
print("After Swap: a =", a, ", b =", b)
```

### 🔽 Output
```
Before Swap: a = 5 , b = 10
After Swap: a = 10 , b = 5
```

### 📘 Explanation
- Python allows a simple way to swap values using `a, b = b, a`.

---

## 15. 📥 Command Line User Input

### ✅ Code
```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name + "! You are", age, "years old.")
```

### 🔽 Output
```
Enter your name: Sumaiya
Enter your age: 22
Hello Sumaiya! You are 22 years old.
```

### 📘 Explanation
- `input()` lets users enter values during runtime.
- Values are taken as strings by default.

---

## 16. 🔎 If-Elif-Else Statements

### ✅ Code
```python
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```

### 📘 Explanation
- Use `if`, `elif`, and `else` to control flow based on conditions.

---

## 17. 🔁 While Loop

### ✅ Code
```python
i = 1
while i <= 5:
    print("Count:", i)
    i += 1
```

### 📘 Explanation
- A `while` loop runs until the condition becomes false.

---

## 18. 🔂 For Loop

### ✅ Code
```python
for i in range(1, 6):
    print("Number:", i)
```

### 📘 Explanation
- `for` loop is used to iterate over sequences like `range()`.

---

## 19. 🚦 Break, Continue, Pass

### ✅ Code
```python
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    if i == 1:
        pass
    print(i)
```

### 🔽 Output
```
0
1
3
```

### 📘 Explanation
- `break` exits the loop early.
- `continue` skips the current iteration.
- `pass` does nothing — placeholder.

---

## 20. 🔍 Break vs Continue vs Pass

### ✅ Code
```python
print("Break example:")
for i in range(5):
    if i == 3:
        break
    print(i)

print("\nContinue example:")
for i in range(5):
    if i == 3:
        continue
    print(i)

print("\nPass example:")
for i in range(5):
    if i == 3:
        pass
    print(i)
```

### 📘 Explanation
- This compares how `break`, `continue`, and `pass` behave in loops.

---

## 21. ⭐ Printing Pattern

### ✅ Code
```python
for i in range(1, 6):
    print("*" * i)
```

### 🔽 Output
```
*
**
***
****
*****
```

### 📘 Explanation
- Repeating `*` character using string multiplication.

---

## 22. 🔁 For-Else Loop

### ✅ Code
```python
for i in range(3):
    print("Try:", i)
else:
    print("No Break - Else block executed")
```

### 📘 Explanation
- `else` runs if the loop wasn't exited with `break`.

---

## 23. 🔍 Prime Number Check

### ✅ Code
```python
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
```

### 📘 Explanation
- Prime numbers are only divisible by 1 and itself.
- `else` after `for` confirms no divisors were found.

---

> ✅ Keep practicing by changing the numbers and logic!
