num=121
result=""
org=num

while(num!=0):
    digit=num%10
    result=result+str(digit)
    num=num//10
if int(result)==org:
    print("palindrome")
else:
    print("not palindrome")



