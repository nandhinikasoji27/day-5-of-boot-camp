# input: hello-----wor----ld
# output: ---------hello world

inp="hello-----wor----ld"
newstr=inp.replace('-','')
str=inp.count('-')
result='-'*str+newstr

print(result )


inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)