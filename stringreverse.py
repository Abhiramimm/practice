string="hello"
result=""
for i in range(len(string)-1,-1,-1):
    result=result+string[i]
print(result)