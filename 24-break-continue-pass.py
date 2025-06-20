# Demonstrating break, continue, and pass
for i in range(5):
    if i == 2:
        continue  # skips 2
    if i == 4:
        break     # stops at 4
    if i == 1:
        pass      # does nothing
    print(i)
