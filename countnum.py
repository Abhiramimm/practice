lst= [1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1]

nc={num:lst.count(num) for num in set(lst)}
print(nc)

for k,v in nc.items():
    if max(nc.values())==v:
        print(k)

