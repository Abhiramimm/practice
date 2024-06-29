text="THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

isPanagram=True

for ch in alphabets:

    if ch not in text:

        isPanagram=False

        break
    
print(isPanagram)