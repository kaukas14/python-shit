# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i += 1 
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
#     print(num)

def funkcija(amount,increment):   ## Tabulecija svarbu su funkcijom ir ciklais
    i = increment
    numbers = []
    while i < amount:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1 
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")

    for num in numbers:
        print(num)

funkcija(6,2)

def with_range(amount,increment):
    numbers = []
    for increment in range(increment,amount):
        print(f"At the top i is {increment}")
        numbers.append(increment)

        print("Numbers now:", numbers)
        print(f"Ar the bottom i is {increment}")
    print("the numbers:")

    for num in numbers:
        print(num)

with_range(6,2)  # abi funkcijos padaro ta pati