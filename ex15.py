#reading file
from sys import argv # inport argumentas module and define agruments in line below

script, filename = argv #pylint: disable=unbalanced-tuple-unpacking

#filename = input("name file to read")
txt = open(filename)  # set var txt as content's of file given

print(f"Here's your file {filename}:") 
print(txt.read())           # reads var to console

txt.close()  # not to forget to close files

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
# txt_again.close() closes file with this outcome is 
# > ex12.py
# Traceback (most recent call last):
#   File "ex15.py", line 19, in <module>
#     print(txt_again.read())
# ValueError: I/O operation on closed file.
print(txt_again.read())
txt_again.close()