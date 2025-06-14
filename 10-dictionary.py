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
