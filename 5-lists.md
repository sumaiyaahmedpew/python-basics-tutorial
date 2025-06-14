#  Lists in Python

A **list** is an ordered collection of items. You can store multiple values in a single variable using a list.

---

##  Example Code

```python
# Creating a list of fruits
fruits = ["apple", "banana", "cherry", "mango"]

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding a new fruit
fruits.append("orange")
print("After adding:", fruits)

# Removing a fruit
fruits.remove("banana")
print("After removing:", fruits)

# Looping through list
print("All fruits:")
for fruit in fruits:
    print(fruit)





## Output
First fruit: apple
Last fruit: mango
After adding: ['apple', 'banana', 'cherry', 'mango', 'orange']
After removing: ['apple', 'cherry', 'mango', 'orange']
All fruits:
apple
cherry
mango
orange

## Explanation
- fruits = [...] creates a list.
- fruits[0] accesses the first item.
- fruits[-1] accesses the last item.
- append() adds a new item to the end.
- remove() deletes an item from the list.
- for fruit in fruits: loops through all items.






