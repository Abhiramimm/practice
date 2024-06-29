string="madam"
length=len(string)
# print(length)
org=string
result=""

for i in range(len(string)-1,-1,-1):

    result=result+string[i]
# print(result)

if result==org and length==4:

    print("5 points")

elif result==org and length==5:

    print("10 points")

else:

    print(result)

