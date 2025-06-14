# Tuples in Python

A **tuple** is like a list, but it **cannot be changed** (it's immutable).  
Use a tuple when you want to store a fixed set of values.

---

## Example Code

```python
# Creating a tuple of colors
colors = ("red", "green", "blue")

# Accessing elements
print("First color:", colors[0])
print("Last color:", colors[-1])

# Trying to modify a tuple (will cause error if uncommented)
# colors[0] = "yellow"

# Loop through tuple
print("All colors:")
for color in colors:
    print(color)



## Output

First color: red
Last color: blue
All colors:
red
green
blue

## Explanation
- colors = (...) creates a tuple using parentheses.
- colors[0] and colors[-1] access elements just like a list.
- You cannot change a tuple — trying to do so will cause an error.
- Tuples are faster and safer for storing data that shouldn't be modified.



