rows = 7
for i in range (1,rows + 1):
    for j in range (1,rows - i + 1):
        print (end=" ")
    for j in range (1,rows + 1):
        print ("*",end=" ")
    print()