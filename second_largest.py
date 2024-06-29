lst=[20,4,6,8,10]

largest=max(lst)
lst.remove(largest)
second_largest=max(lst)
print(second_largest)

#2 =========================================

lst=[20,4,6,8,10]

lst.sort()
second_largest=lst[-2]
print(second_largest)

# 3======================================
lst=[20,4,6,8,10]
lst.sort()

largest=0
second_largest=0

for num in lst:
    if num>largest:
        second_largest=largest
        largest=num
print(largest)
print(second_largest)


