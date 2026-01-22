t = (10, 20, 30, 40, 50)

print("Original Tuple:", t)

lst = list(t)           
lst[2] = 100           

t = tuple(lst)         

print("Updated Tuple:", t[2])
