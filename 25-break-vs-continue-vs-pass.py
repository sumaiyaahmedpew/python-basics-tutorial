# Difference illustration
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
