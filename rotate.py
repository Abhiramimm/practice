lst=[1,2,3,4,5,6,7]

k=1

for i in range(0,k):
    last_element=lst.pop()
    lst.insert(0,last_element)
print(lst)