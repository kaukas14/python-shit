# si funkcija veikia taip kaip skriptas su argumentais paduodamais konsoles

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# daryti su * argv nera butina
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2 {arg2}")

# su vienu argumentu
def print_one(arg1):
    print(f"arg1: {arg1}")

# be argumentu
def print_none():
    print("I got nothin'.")
    print("does it work") # jei blogai eiliuoji vscode iskart taiso

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()