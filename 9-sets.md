# Sets in Python

A **set** is an unordered collection of unique items.  
It does **not allow duplicates** and the items are **not ordered**.

---

## Example Code

```python
# Creating a set of numbers
numbers = {1, 2, 3, 4, 5}

# Adding a new number
numbers.add(6)

# Removing a number
numbers.remove(3)

# Duplicate values are automatically removed
numbers.add(2)

# Print all elements
print("Set of numbers:", numbers)

# Loop through the set
print("All numbers:")
for number in numbers:
    print(number)


## Output
Set of numbers: {1, 2, 4, 5, 6}
All numbers:
1
2
4
5
6


Explanation
-Sets are created using {} with comma-separated values.
-.add() inserts an element.
-.remove() deletes an element.
-Duplicates are automatically ignored.
-Sets are unordered, so the output order may vary.
-Useful for checking membership, removing duplicates, and set operations like union, intersection.
