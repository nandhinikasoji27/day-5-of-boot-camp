rows = 3
cols = 4

for i in range(0, rows):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(1, cols):
        print("*", end="")
    print()