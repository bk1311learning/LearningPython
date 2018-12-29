from sys import argv #sys is a module that has argv object. this is used for command line arguments

script, filename = argv  #script variable is the name of this script. filename will be the file to be read and will need to be specified on the command line when running the script


txt = open(filename) # This will open contents of filename specified and assign it to txt variable

print(f"Here's your file {filename}:") #prints a string which has avariable of filename specified on the command line
print(txt.read())  #read contents of txt and is printed.

print("Type the filename again:") #prints string asking for prompt
file_again = input("> ") # shows > as to user who inputs a value. value is assinged to file_again.

txt_again = open(file_again) #same as before open the file again and assigns contents to txt_again

print(txt_again.read())  #reads contents of txt_again and prints them
