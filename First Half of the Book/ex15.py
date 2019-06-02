# allows us to use the argv variable from the sys module/library
from sys import argv

# defines the arguements that we are expecting
script, filename = argv

# sets the contents from our filename argument to the txt variable
txt = open(filename)

# printing the name of the file
print(f"Here's your file {filename}:")
# prints the contents of the filename arguement using the read function
print(txt.read())

# asks us for a new filename argument
print("Type the filename again:")
# stores our input to the file_name variable, we have a prompt defined for the input
file_again = input("> ")

# setting the conents of the new filename argument to a variable
txt_again = open(file_again)

# printing the data stored to the variable using the read function
print(txt_again.read())
