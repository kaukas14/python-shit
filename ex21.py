#function with return
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} + {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Lets do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#Puzzle for extra credit
print("Here is a puzzle.")

# what = add(age, subtract(height, multiply(weight, divide(iq,2))))
def get_what(iq, weight,height,age):
    vienas = iq / 2
    du = weight * vienas
    trys = height - du
    what = age + trys
    return what

what = get_what(iq,weight,height,age)
print("That becomes: ", what , "can you do it by hand")