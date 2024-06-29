my_tuple=(1,2,2,3,4,4,5)


frequency={num:my_tuple.count(num) for num in set(my_tuple)}

print(frequency)

