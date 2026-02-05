# write python program to display the number form 1 to 10 except for number 6

i = 1
while i <= 10:
    if i == 6:
        i += 1
        continue
    print(i)
    i += 1

# write python program to display number betweeen 1 to 10 
# after printing number 5 the loop must terminates

print("Number breaking after 5:")
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
   