# 🐍 Python Basics – README Tutorial Guide

This repository contains beginner-level Python programs with clear explanations and outputs. Based on the YouTube tutorial: [Learn Python Programming](https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3)

---

## 06. 🖥️ Python Editor & Hello World

### ✅ Code
```python
print("Hello, Python!")
```

### 🔽 Output
```
Hello, Python!
```

### 📘 Explanation
- `print()` displays a message.
- This is the basic structure of a Python program.
- You can run it in IDLE, VS Code, or any terminal with Python installed.

---

## 07. 🔁 More on Variables

### ✅ Code
```python
x = 10
y = 20
name = "Sumaiya"
x = x + 5
print("Updated x:", x)
print("Name:", name)
```

### 🔽 Output
```
Updated x: 15
Name: Sumaiya
```

### 📘 Explanation
- Variables store data like numbers or text.
- You can update a variable by reassigning it.
- Python is dynamically typed — you don’t need to declare types.

---

## 08. 📦 Data Types in Python

### ✅ Code
```python
name = "Python"
age = 25
height = 5.8
is_programmer = True
skills = ["Python", "SQL"]
info = (1, 2, 3)
marks = {90, 85, 80}
details = {"name": "Sumaiya", "age": 22}
print(type(name), type(age), type(height), type(is_programmer))
```

### 🔽 Output
```
<class 'str'> <class 'int'> <class 'float'> <class 'bool'>
```

### 📘 Explanation
- Python has multiple data types: string, int, float, bool, list, tuple, set, and dict.
- `type()` function shows the data type of any variable.

---

## 09. ➕ Operators in Python

### ✅ Code
```python
a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Is a > b and b < 10?", a > b and b < 10)
```

### 🔽 Output
```
Addition: 19
Subtraction: 11
Multiplication: 60
Division: 3.75
Floor Division: 3
Modulus: 3
Exponent: 50625
Is a > b and b < 10? True
```

### 📘 Explanation
- Python supports arithmetic and logical operators.
- Logical operators: `and`, `or`, `not`
- Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`

---

## 10. 🔢 Number System Conversion

### ✅ Code
```python
num = 25
print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))
```

### 🔽 Output
```
Binary: 0b11001
Octal: 0o31
Hexadecimal: 0x19
```

### 📘 Explanation
- `bin()`, `oct()`, and `hex()` are used to convert numbers into binary, octal, and hex.

---

## 11. ⬆️ IDLE Previous Command

### 📘 Explanation
- In Python’s **IDLE**, you can use the **Up Arrow key** to bring back previous commands.
- Saves time by letting you re-run or edit earlier code.

---

## 12. 🧠 Bitwise Operators

### ✅ Code
```python
a = 10  # 1010
b = 4   # 0100
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT a:", ~a)
print("Left Shift a by 2:", a << 2)
print("Right Shift b by 1:", b >> 1)
```

### 🔽 Output
```
AND: 0
OR: 14
XOR: 14
NOT a: -11
Left Shift a by 2: 40
Right Shift b by 1: 2
```

### 📘 Explanation
- Bitwise operations are done on the binary representation of integers.
- Used in low-level programming, optimizations, and performance-critical code.

---

## 13. 📐 Using Math Module

### ✅ Code
```python
import math
print("Square root of 16:", math.sqrt(16))
print("Power 2^3:", math.pow(2, 3))
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print("Log base 10 of 100:", math.log10(100))
```

### 🔽 Output
```
Square root of 16: 4.0
Power 2^3: 8.0
Sine of 90 degrees: 1.0
Log base 10 of 100: 2.0
```

### 📘 Explanation
- The `math` module includes functions like square root, trigonometry, power, log, etc.
- `math.radians()` is used to convert degrees to radians before applying trigonometric functions.

---
