
str=input()
vowels="aeiou"
consonants= "bcdfghjklmnpqrstvwxyz"
inp=str.lower()
for i in inp:
    if(i in vowels):
        print(i,end="")
for i in inp:
    if(i in consonants):
        print(i,end="") 
         