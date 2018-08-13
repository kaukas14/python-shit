# argumentai i skripta
from sys import argv
# read the WYSS section for how to run this
nulis, first, second, third = argv #pylint: disable=unbalanced-tuple-unpacking
spalva = input("kokia spalva:")

print("The script is called:", nulis) # idomu kad skripto pavadinima paima kaip pirma argumenta. 
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print(f"Spalva {spalva}")