# rows = 5
# columns = 5
# for i in range(rows):
#     for j in range(columns):
#         print('*', end='  ')
#     print()




r=6
c=7
for i in range(r):
    for j in range(c):
        if(i==j):
            print(" ",end="")
        else:
            print("*",end="")
    print()    