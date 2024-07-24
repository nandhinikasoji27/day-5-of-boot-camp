str=input()
vowels="aeiou"
consonants= "bcdfghjklmnpqrstvwxyz"
inp=str.lower()
ans=""
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)        