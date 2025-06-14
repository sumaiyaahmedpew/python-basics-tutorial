# 📚 Dictionary in Python

A **dictionary** is a collection of key-value pairs.  
It allows you to store and access data using keys.

---

## ✅ Example Code

```python
# Creating a dictionary
student = {
    "name": "Sumaiya",
    "age": 22,
    "is_student": True,
    "courses": ["Python", "SQL"]
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])
print("Is Student:", student["is_student"])
print("Courses:", student["courses"])

# Adding a new key-value pair
student["grade"] = "A"

# Updating a value
student["age"] = 23

# Removing a key
del student["is_student"]

# Looping through dictionary
print("\nStudent Information:")
for key, value in student.items():
    print(key + ":", value)



## Output

Name: Sumaiya
Age: 22
Is Student: True
Courses: ['Python', 'SQL']

Student Information:
name: Sumaiya
age: 23
courses: ['Python', 'SQL']
grade: A



Explanation
- A dictionary uses {} with key-value pairs.
- Keys are unique and can be strings or numbers.
- Values can be of any data type.
  Such as:
           Access: student["name"]
           Add: student["grade"] = "A"
           Update: student["age"] = 23
           Delete: del student["is_student"]

- .items() lets you loop through key-value pairs.


