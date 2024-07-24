# # write a program for consonats count


# check=['a','e','i','o','u']
# count=0
# count1=0
# inp="nandhinikasoji"
# for i in inp:
#     if(i in check):
#         count+=1
#     else:
#         count1+=1
# print(count) 
# print(count1)  


str=input()
inp=str.lower()
vowels="aeiou"
v=0
c=0
consonants="bcdfghjklmnpqrstvwxyz"
for i in inp:
    if(i in vowels):
        v+=1
for i  in inp:
    if (i in consonants):
        c+=1
print(v)
print(c)         
