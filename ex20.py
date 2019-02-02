# Functions and files
from sys import argv #importing library

input_file = argv[1] # seting first imput file as value for var imput_file

def print_all(f):  # define function which read given file
    print(f.read())

def rewind(f): #moves reading head to begining of file
    f.seek(0)

def print_a_line(line_count, f): #function to print specific line
    print(line_count, f.readline())

current_file = open(input_file) # setting var current_file to text from given input file

print("First let's print the whole file:\n")

print_all(current_file) # calling function by giving value current_file

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # calling function rewind to go back to beggining of file, if not since file was open and read reading head would stay at end and it wont print lines

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)