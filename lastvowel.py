text="welcome"
last_element=text[-1]
vowels=["a","e","i","o","u","A","E","I","O","U"]

if last_element in vowels:
    print(text[:-1])
else:
    print(text)
