num1=30
num2=45
gcd=1
smallest= num1 if num1<num2 else num2

for i in range(1,smallest):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)
