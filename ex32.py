the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges','pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for loop goes throught a list

for number in the_count:
    print(f"This is count {number}")

# same as above

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go throught mixed list too
#notice we have to use {} since we dont know whats in it

for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an emply one
elements = list(range(5))  # range(5) nuo 0 iki 4 
for i in elements:
    print(f"Elements with range: {i}")

# then use the range function to do 0 to 5 counts
for i in range(0, 6):  #range pirmas itraukiamas o antras ne
    print(f"Adding {i} to the list")
    # append is a function that listts understand  appent prideda i esama nebutinai tuscia
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

sarasioks = [[1,2,3],[4,5,6]] # array toks labiau
for i in sarasioks:
    print(f"narys: {i[1]}")