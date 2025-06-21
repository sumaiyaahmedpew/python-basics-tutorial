# Taking array values from user
size = int(input("Enter number of elements: "))
user_arr = []
for i in range(size):
    val = int(input(f"Enter element {i+1}: "))
    user_arr.append(val)
print("User array:", user_arr)
