#set
set_ds = {1, 3, 2, 4, 4, 5, 6, 7 ,2,  5, 7, 8}
print(set_ds) # output {1, 2, 3, 4, 5}duplicates not allowed

set_ds.add(55)
print(set_ds)

set_ds.remove(55)
print(set_ds)

#operations
set_ds1 = {10,20,30,40,50}
set_ds2 = {10,20,100,200,300}

print(set_ds1.union(set_ds2)) # {1,2,3,4,5,10,20,30,40,50,100,200,300}
print(set_ds1.intersection(set_ds2)) # {10,20}
print(set_ds1.difference(set_ds2)) # {30,40,50}
