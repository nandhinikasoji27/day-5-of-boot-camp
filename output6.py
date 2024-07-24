# hello 123 the output should be 6

vowels="aeiou"
consonants= "bcdfghjklmnpqrstvwxyz"
check="0123456789"
ans=0
i="hello 123"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
print(ans)        
