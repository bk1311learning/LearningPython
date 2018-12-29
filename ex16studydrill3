from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
#Here we are opening the file with mode W. This is write mode. By default
#open will open in read mode, so adding w will allow us to write to the file later
#NOTE when you open a file W mode it actually truncates it first (empties)
#using mode a will allow you to open for writing appending to the end of the file
target = open(filename, 'w')


print("Truncating the file. Goodbye!")
#below truncates the file, not needed however as opening in w already does this.
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

#this writes contents of the input variables from above, adding a new line
#between variables
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.close()
target2 = open(filename, 'r')
#closes open file
print(f"{filename} contains the below contents")
print(target2.read())
print("And finally, we close it.")
target2.close()
