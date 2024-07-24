# #print how many vowels are in a string

# inp = input('Enter the string :')
# count = 0
# inp= inp.lower()
# for i in inp:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         count+=1
# if count == 0:
#     print('No vowels found')
# else:
#     print('Total vowels are :' + str(count))



check=['a','e','i','o','u']
count=0
inp="nandhinikasoji"
for i in inp:
    if(i in check):
        count+=1
print(count)        